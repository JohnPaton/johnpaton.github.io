[![Build Status](https://travis-ci.com/JohnPaton/johnpaton.github.io.svg?branch=dev)](https://travis-ci.com/JohnPaton/johnpaton.github.io)

# johnpaton.net

This is the source repository for [johnpaton.net](https://johnpaton.net), which is built with [Pelican](https://blog.getpelican.com/), deployed with [TravisCI](https://travis-ci.com), and served by [GitHub Pages](https://pages.github.com/). 

## Development

The source for building the website is located in the [`dev` branch](https://github.com/JohnPaton/johnpaton.github.io/tree/dev). To get started, clone the repository and also its submodules, and install the requirements:

```bash
$ git clone -b dev git@github.com:JohnPaton/johnpaton.github.io.git
$ cd johnpaton.github.io
$ git submodule update --init --recursive
$ pip3 install -r requirements.txt
```

The [settings for the Pelican build](https://docs.getpelican.com/en/3.7.1/settings.html) are in `pelicanconf.py`. All the website content is stored in the `content` directory. To make changes, edit the markdown files there or make a new one. To preview your changes, from the repository root run:

```bash
$ pelican -ds pelicanconf.py
```

The generated site will be written to the `output` directory. As an alternative to rebuilding every time, you can also run `make devserver` to start a development server at `http://localhost:8000`. Every time a change is detected in one of the source files, the output will be regenerated, so you just have to refresh the page you're working on to see the changes to the source reflected.

## Deployment

To deploy changes to the site, the generated contents of `output` need to be committed to the `master` branch, which is where GitHub Pages serves the site from. This is currently handled by [TravisCI](https://travis-ci.com/JohnPaton/johnpaton.github.io) and their super handy [GitHub Pages Deployment](https://docs.travis-ci.com/user/deployment/pages/), with a new deployment being triggered by any new commits being pushed to the `dev` branch. Don't forget to save a Personal Access Token to the `GITHUB_TOKEN` environment variable in Travis!

Pelican setting overrides for deployment (e.g. changing the host for generated links from `localhost:8000` to `johnpaton.net`) are stored in `publishconf.py`.
