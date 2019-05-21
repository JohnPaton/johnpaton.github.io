title: Redirect Standard Out to Python's logging module with contextlib
slug: redirect-logging
date: 2019-05-20 17:00:00 UTC+01:00
tags: python
type: text
cover: 
author: John Paton
summary: 
status: draft

Python's logging functionality is very nice once you get the hang of it, but many people (including library developers) either disagree or don't bother to use it. Instead, you often see things like this:

```python
>>> model.fit(X, y, verbose=True)
Epoch 0
Epoch 1
Epoch 2
...
```
and onwards for 100 lines or whatever. 

Writing status messages to standard out is _okay_, but if you want anything like consistent/parsable logs, log level handling, logging to multiple locations, etc. this can get a bit annoying. How can we redirect standard out to Python's logging system to get all these juicy benefits?

Another builtin module, `contextlib`, comes to our rescue.

## Aside: Context Managers

Roughly speaking, a context manager in Python is an object that implements 2 methods: `__enter__` and `__exit__`. Usually you enter the context by using the `with` keyword, which triggers a call to `__enter__`. You execure some code in an indented block, and (roughly speaking) when you exit the block, the `__exit__` method is called. The context manager interface is what makes these two pieces of code more or less equivalent:

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

The file handle returned by `open` implements `__enter__` and `__exit__`, which is why it can be used in this way. The nice benefit here is that we never forget to close the file, as `__exit__` is called automagically at the end of the block.

## Redirecting `stdout`

So how does this help us? Well, `contextlib` (which is the library for htings related to context managers, in case you didn't catch that) has a very handy context manager called `redirect_stdout` (and also the matching `redirect_stdin`). We can use it to redirect text written to standard out to another file-like object. For example, to write to a file, we could do:

```python
>>> import contextlib
>>> with open("output.txt", "w") as h, contextlib.redirect_stdout(h):
...     print("Hello world!")
>>>
```
We don't see any output. If we now look at the newly-created `output.txt`, we will see

```
$ cat output.txt
Hello world!
```

I realize that there are better ways of writing to a file in Python, but writing to a file isn't the point. The point is that any arbitrary code executed in the context block above would have its output redirected to the file, _without_ having to modify its print statements, including library code that we can't easily modify. 

Now, `redirect_stdout` requires a file-like object that it can `write` to, which is why we first had to `open` out output file above. However, Python's loggers are not file-like. I think you see where this is going.


## A file-like logger

## Baby's first context manager

What we can do is the following:

* Create a class that implements a subset of the file-like interface (in this case we only really need `write`)
* Make our `write` pass messages to a logger
* Also implement our own context manager interface, where we pass our `self` to `redirect_stdout` so that anything that gets written in our context actually is redirected to the logger
* Clean everything up when we exit

This sounds complicated, but it turns out actually to be quite easy. Here is a barebones implementation:


## Disclaimer









