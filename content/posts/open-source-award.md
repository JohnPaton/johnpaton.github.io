title: Receiving a Google Open Source Peer Bonus award
slug: open-source-award
date: 2020-05-07 11:00:00 UTC+01:00
tags: python, open source, pandas
category: 
cover: images/google-ospb.png
link: 
status: 
description:
type: text
author: John Paton
summary: Over the past few years I've increasingly tried to make small [contributions](https://github.com/search?q=author%3AJohnPaton+is%3Apr&type=Issues) to open source projects that I use. I'm not on the core team of any one project, so usually my contributions are very small. That's why I was very surprised when I got an email from Google's Open Source Peer Bonus program, letting me know that I had been nominated!

Over the past few years I've increasingly tried to make small [contributions](https://github.com/search?q=author%3AJohnPaton+is%3Apr+is%3Amerged) to open source projects that I use. Usually these come from me encountering a small issue that I know [how to fix](https://github.com/kubeflow/kubeflow/pull/3107), or lightly improving the documentation. Occasionally I've also used the process of "making your first contribution" to get to know a tool [from the inside](https://github.com/tiangolo/fastapi/pull/1106). I'm not a developer, and I'm also not on the core team of any one project, so usually my contributions are [very small](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/pull/1183). That's why I was very surprised a few weeks ago when I got an email from Google's [Open Source Peer Bonus](https://opensource.google/docs/growing/peer-bonus/) program, letting me know that I had been nominated! 

[![OSPB logo](/images/google-ospb.png)](https://opensource.googleblog.com/2020/01/announcing-2019-second-cycle-google.html)

It turns out that Google's employees who maintain open source projects can nominate contributors as a thank you from Google and from the community. Receiving the award gets you a nice letter, a mention in their [blog post](https://opensource.googleblog.com/2020/01/announcing-2019-second-cycle-google.html), and a small cash prize. I was nominated for contributing to the Python client libraries for [Google BigQuery](https://cloud.google.com/bigquery) ([`google-cloud-python`](https://github.com/googleapis/google-cloud-python/tree/master/bigquery) and its pandas-compatible layer, [`pandas-gbq`](https://github.com/pydata/pandas-gbq)), which we use every day at [Catawiki](https://www.catawiki.com/jobs). 

These were the contributions I was nominated for:

* [pydata/pandas-gbq#256](https://github.com/pydata/pandas-gbq/pull/256): My first time contributing to one of these projects, this PR was just a simple cleanup of a usage example in the documentation. More of a nitpick than anything else, but they reacted in a friendly way which made it much less scary to contribute actual code in the future.

* [pydata/pandas-gbq#257](https://github.com/pydata/pandas-gbq/pull/257): This one was an actual feature for pandas-gbq. When you upload a DataFrame to BigQuery, pandas-gbq generates a schema for your table based on the pandas dtypes. Alternately, you can provide your own schema if you want more control, e.g. when dealing with time columns (`DATE`? `DATETIME`? `TIMESTAMP`?). This PR added the ability to provide a schema for only a subset of columns and to fall back to the generated schema for the rest, which is handy if you have a very wide DataFrame and you only want to cast a few columns.

* [googleapis/google-cloud-python#7552](https://github.com/googleapis/google-cloud-python/pull/7552): I'm a simple man. I see incremental progress, I want a progress bar. This PR, which originally started as a [feature request](https://github.com/pydata/pandas-gbq/issues/182) on pandas-gbq, added a [`tqdm`](https://tqdm.github.io/) progress bar to Google's BigQuery client when downloading data from BigQuery. I personally wanted this as I was spending a non-negligible amount of time in those days downloading large-ish training sets. As you'll see in the comments of the PR, I got a ton of feedback about my initial commits. It was all very friendly and I learned a lot about the code-review process among real software engineers. In the end, my original request to include this feature in pandas-gbq (and not just google-cloud-python) was actually [implemented by someone else](https://github.com/pydata/pandas-gbq/pull/292)! All around a cool example of open source in action.

It's pretty common to be afraid of contributing to open source projects because you're worried about making mistakes, being criticized, etc. For data scientists, I expect this to be even worse as you likely have the added layer of impostor-syndrome from not being a "real" software developer. But if you have tools that you use often and that make your life better, then you get to know them and their quirks pretty quickly, which makes it easier to get started. And maintainers of projects are often very happy to know that people care and want to contribute, especially if you read their `CONTRIBUTING.md` or other contribution guidelines first. At the time of writing, there are over [15,000 open "good first issues" in Python projects on GitHub](https://github.com/search?l=Python&o=desc&q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22&s=&type=Issues), specifically tagged for people looking to get involved for the first time. Why not give it a try and dive in?
