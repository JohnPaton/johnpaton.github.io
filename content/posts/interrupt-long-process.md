title: Schedule the interruption of hung Python processes with signals
slug: interrupt-long-processes
date: 2019-07-13 13:00:00 UTC+01:00
tags: python, snippets
category: 
link: 
status:
description:
type: text
author: John Paton
summary: A lightweight method to interrupt (hung) Python processes after a set time using the `signal` library.

At Catawiki, we have a lot of scheduled cron-type jobs that move data around, train models, and do other processing tasks. Often, they are dependent on external resources like database connections. If one of these jobs actually fails, emails are sent, and we can fix the problem. However, we have had issues in the past with scheduled jobs silently hanging, which can often go unnoticed until someone's output hasn't been refreshed. One solution to this would be to schedule these small jobs in our Airflow pipeline, but for little things that just need to run every night without hassle we use this lightweight trick instead.

To make a Python process fail and get a precious notification, we can force it to raise a `TimeoutError` after a certain number of seconds using the [`signal` library](https://docs.python.org/3/library/signal.html). This library is responsible for handling [Unix Signals](https://en.wikipedia.org/wiki/Signal_(IPC)), which are a way to communicate asynchronously with running processes.

**Note:** If you are doing fancy stuff with multiple threads, please read the signal docs as there can be weird behavior here. Also, alarm scheduling is only available on Unix-like systems.

Technically Step 3 below is already enough to cause the timeout by itself, but your output will be very terse. Defining the signal handler with a friendly message ensures that both your colleagues and your future self will be able to read your code and your logs.

## Step 1: Define a Signal Handler

A signal handler is a function that can be called when a signal is received. Signal handlers must accept [two arguments](https://docs.python.org/3/library/signal.html#signal.signal), but our handler will just ignore them and raise a `TimeoutError`:

```python
import signal

def timeout_handler(sig, frame):
    raise TimeoutError("Your process has timed out!")
```

Raising an exception will interrupt the process, killing whatever was going on. If this is too extreme and you just want to be alerted that a process is still running without killing it, you could also do something like send an email or send yourself a [Slack message](https://github.com/slackapi/python-slackclient#sending-a-message-to-slack):

```python
import os
import slack

def slack_handler(sig, frame):
    # Don't keep your token in plain text :)
    token = os.environ["SLACK_API_TOKEN"]
    client = slack.WebClient(token=token)

    client.chat_postMessage(
        channel="#python_alerts",
        text="Your process is still running!"
    )
```

## Step 2: Assign the signal hander to the alarm signal

Next we use [ `signal.signal` ](https://docs.python.org/3/library/signal.html#signal.signal) to tell Python that our new handler should be called whenever the running process receives the alarm signal, denoted by `signal.SIGALRM`. 

```python
# Call `timeout_handler` when we receive an alarm signal
signal.signal(signal.SIGALRM, timeout_handler)
```

## Step 3: Schedule an alarm

Now we can [schedule an alarm](https://docs.python.org/3/library/signal.html#signal.alarm) to be sent to our process after a set number of seconds. If the process has exited before that time has passed, nothing will happen. If the process is still running when the alarm is sent, then our handler will be called, interrupting the process and raising an exception. If you're going to interrupt a process, this timeout should be comfortably longer than you expect the process to take, so that it is only interrupted if something is really stuck.

```python
# Schedule an alarm to be sent in 10 seconds 
signal.alarm(10)
```

You can now run your main loop or do whatever work you are trying to do, and you're guaranteed that the process will fail if it takes longer than the time you specified. 

If you are writing a module with functions that might get imported elsewhere, make sure to put the `signal.signal` and `signal.alarm` lines under your `if __name__ == "__main__"` statement so that the alarm doesn't get triggered every time your module is imported.

## Complete Example

```python
# timeout.py
import signal  

def timeout_handler(sig, frame):
    raise TimeoutError("Your process has timed out!")

# Call `timeout_handler` when we receive an alarm signal
signal.signal(signal.SIGALRM, timeout_handler)

# --- Example Usage

# Schedule an alarm in 10 seconds 
# (will raise TimeoutError as specified)
signal.alarm(10)

# Do some work which takes too long
import time
i = 0
while True:
    print(i, "seconds passed")
    i += 1
    time.sleep(1)
```

Running our example yields the following output:

```console
$ python timeout.py
0 seconds passed
1 seconds passed
2 seconds passed
3 seconds passed
4 seconds passed
5 seconds passed
6 seconds passed
7 seconds passed
8 seconds passed
9 seconds passed
Traceback (most recent call last):
  File "timeout.py", line 21, in <module>
    time.sleep(1)
  File "timeout.py", line 5, in timeout_handler
    raise TimeoutError("Your process has timed out!")
TimeoutError: Your process has timed out!
exit 1
```
