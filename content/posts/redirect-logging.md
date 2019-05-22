title: Redirect standard out to Python's logging module with contextlib
slug: redirect-logging
date: 2019-05-20 17:00:00 UTC+01:00
tags: python, snippets
type: text
cover: images/logs_cover.jpg
author: John Paton
summary: Python's logging functionality is very nice once you get the hang of it, but many people either disagree or don't bother to use it. Learn how to redirect other people's pesky print statements into your nice logging setup.
status: draft

![Logging](/images/logs_cover.jpg)
<div style="text-align:center"><small>[Logging](https://en.wikipedia.org/wiki/Logging) on Wikipedia</small></div>

Python's built in logging functionality is very nice once you get the hang of it, but many people (including library developers) either disagree or don't bother to use it. Instead, you often see things like this:

```python
>>> model.fit(X, y, verbose=True)
Epoch 0
Epoch 1
Epoch 2
...
```
and onwards for 100 lines or whatever. 

Printing status messages to standard out is _okay_, but if you want anything like consistent/parseable logs, log level handling, logging to multiple locations, etc. this can get a bit annoying. How can we redirect standard out to Python's logging system to get all these juicy benefits?

Another built in module, `contextlib`, comes to our rescue.

## Aside: Context Managers

A [context manager](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers) in Python is basically an object that implements two methods: `__enter__` and `__exit__`. Usually you enter the context by using the `with` keyword, which triggers a call to `__enter__`. You execute some code in an indented block, and (roughly speaking) when you exit the block, the `__exit__` method is called with information about any exceptions that occurred. The context manager interface is what makes these two pieces of code more or less equivalent:

```python 
h = open("file.txt")
text = h.read()
h.close()
```
is basically the same as

```python
with open("file.txt") as h:
    text = h.read()
```

The file handle returned by `open` implements both `__enter__` and `__exit__`, which is why it can be used in this way. The nice benefit here is that we never forget to close the file, as `__exit__` (which closes the file in this case) is called automagically at the end of the block.

## Redirecting `stdout`

So how does this help us? Well, `contextlib` (which is the library for things related to context managers, in case you didn't catch that) has a very handy context manager called `redirect_stdout` (and also the matching `redirect_stderr`). We can use it to redirect text written to standard out to another file-like object. For example, to write to a file, we could do:

```python
>>> import contextlib
>>> with open("output.txt", "w") as h, contextlib.redirect_stdout(h):
...     print("Hello world!")
...
>>>
```
We don't see any output. If we now look at the newly-created `output.txt`, we will see

```
$ cat output.txt
Hello world!
```

I realize that there are better ways of writing to a file in Python, but writing to a file isn't the point. The point is that any arbitrary code executed in the context block above would have its output redirected to the file, _without_ having to modify its print statements, including library code that we can't easily modify. 

Now, `redirect_stdout` requires a file-like object that it can `write` to, which is why we first had to `open` our output file above. However, Python's loggers are not file-like. I think you see where this is going.

## A file-like logger

To redirect standard out to `logging`, we write a simple class that implements the `write` method, and passes everything that is written to the logger of our choice. We'll also add a `flush` method that doesn't do anything, just to avoid exceptions in case some code tries to use it. We can specify the desired logger by name since Python's loggers are [singletons](https://docs.python.org/3/library/logging.html#logger-objects).

```python
import logging
import contextlib

class OutputLogger:
    def __init__(self, name="root", level="INFO"):
        self.logger = logging.getLogger(name)
        self.name = self.logger.name
        self.level = getattr(logging, level)

    def write(self, msg):
        if msg and not msg.isspace():
            self.logger.log(self.level, msg)

    def flush(self): pass
```
I added a quick check for empty messages since I don't want blank lines in my logging. 

This is already enough to pass our object to `redirect_stdout` and thereby redirect standard out to `logging`:

```python
>>> logging.basicConfig(level=logging.INFO)
>>> with contextlib.redirect_stdout(OutputLogger("my_logger", "INFO")):
...     print("Hello logging!") 
...
INFO:my_logger:Hello logging!
```

Note that we had to minimally call `logging.basicConfig()` to get a bit of formatting on the logs and set the log level to at least the level we selected for our redirector (`INFO`). Since our class is just functioning as a redirector for messages, we leave ourselves free to configure the logger however we want elsewhere in the application (check out the [Python logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html) for tips).

## Baby's first context manager

This implementation is already functional, but it's a bit verbose. Since we're already in the `contextlib` realm we might as well just make our object into a context manager itself, eliminating the need to call `contextlib.redirect_stdout` directly every time we want to use it. To do so, we add a new attribute called `_redirector` to our class, which is an instance of `redirect_stdout` with `self` as the redirect destination. Then our `__enter__` and `__exit__` methods just call the matching methods of our `_redirector`, ensuring that everything printed in our context will get redirected to our own `write` method (which in turn passes messages to our `logger`). Our implementation becomes:

```python
import logging
import contextlib

class OutputLogger:
    def __init__(self, name="root", level="INFO"):
        self.logger = logging.getLogger(name)
        self.name = self.logger.name
        self.level = getattr(logging, level)
        self._redirector = contextlib.redirect_stdout(self)

    def write(self, msg):
        if msg and not msg.isspace():
            self.logger.log(self.level, msg)

    def flush(self): pass

    def __enter__(self):
        self._redirector.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # let contextlib do any exception handling here
        self._redirector.__exit__(exc_type, exc_value, traceback)
```

Now we're cooking! We can use `OutputLogger` as a context manager, and since we returned `self` from `__enter__` we can even reuse the same instance later by giving it a name using the `as` keyword:

```python
>>> print("Normal")
Normal
>>>
>>> with OutputLogger("my_logger", "WARN") as redirector:
...     print("Logged!")
...
WARNING:my_logger:Logged!
>>>
>>> print("Back to normal")
Back to normal
>>> 
>>> with redirector:
...     print("Logged again!")
...
WARNING:my_logger:Logged again!
```

There are all sorts of extensions possible here: redirecting standard error to another log level, making sure that changes to `OutputLogger.name` and `OutputLogger.level` get applied to the underlying logger properly, input checking on the log level string, etc. But this is enough to get started and will work as a quick and relatively clean way to capture the output from some other code and redirect it to your application's logging system.

## Disclaimer

Though `contextlib.redirect_stdout` is built in to Python, it does redefine `sys.stdout` for your whole process while the execution is within its context. For this reason, it can have unintended results for other pieces of code that are trying to do fancier stuff with `sys.stdout` than just write to it. This is a solution if you are writing an application that just needs to get something done, but if you are writing a library that other people might use, it's best not do mess with these system properties without being very explicit about it. As always: Just because you can, doesn't mean you should!


<small><small>Cover image by <a rel="nofollow" class="external text" href="https://flickr.com/people/7787236@N07">Greenpeace Finland</a> - originally posted to <a href="//commons.wikimedia.org/wiki/Flickr" class="mw-redirect" title="Flickr">Flickr</a> as <a rel="nofollow" class="external text" href="https://flickr.com/photos/7787236@N07/3227543977">Logging in Finnish Lapland: ancient trees for pulp and paper</a>, <a href="https://creativecommons.org/licenses/by/2.0" title="Creative Commons Attribution 2.0">CC BY 2.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=11805001">Link</a></small></small>