title: Syntax highlighting for console sessions
slug: console-highlighting
date: 2020-11-21 14:00:00 UTC+01:00
tags: snippets, open source
category: 
cover: images/console-syntax-highlighting.png
link: 
status:
description:
type: text
author: John Paton
summary: It's a minor annoyance that comes up often in GitHub comments: syntax highlighting for Python console sessions. You want the input code (after the prompt) to be highlighted, but the output (which is generally just text or logs) to remain neutral. Turns out there's a syntax highlighter that does just that.

It's a minor annoyance that comes up often in GitHub comments: syntax highlighting for Python console sessions. You want the input code (after the prompt) to be highlighted, but the output (which is generally just text or logs) to remain neutral. As far as I can tell, most people opt for one of two options: no highlighting at all (boring, can be harder to read), or Python syntax highlighting (looks nicer but probably makes all kinds of weird colors in your output). 

Here's a classic example where the output includes a progress bar:

```
>>> my_str = "hello"
>>> some_int = 123
>>> func_with_output(a=1, b=my_str)
Processing: 100%|██████████████████| 10/10 [00:01<00:00,  9.71it/s]
```

We would like to spruce this up a bit with some syntax highlighting. If we start our code block with ````python` instead of just the plain regular triple backticks (which start a code block in Markdown), we end up with something that looks like

```python
>>> my_str = "hello"
>>> some_int = 123
>>> func_with_output(a=1, b=my_str)
Processing: 100%|██████████████████| 10/10 [00:01<00:00,  9.71it/s]
```

This is _okay_, but the progress bar look silly and it makes it more difficult to tell what's input and what's output. However, there is actually another syntax highlighter specifically for this case: `pycon` (instead of `python`). it highlights lines that start with the Python prompt (`>>>`), but doesn't highlight output lines which don't have any prompt, leaving us with:

```pycon
>>> my_str = "hello"
>>> some_int = 123
>>> func_with_output(a=1, b=my_str)
Processing: 100%|██████████████████| 10/10 [00:01<00:00,  9.71it/s]
```

As a bonus, for shell sessions (which usually have a less obvious prompt, making it more important to distinguish input from output), you can do the same thing using the `console` highlighter!

```console
$ echo "output colored differently"
output colored differently
```

Perfection.