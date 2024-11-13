[![Deploy to GitHub Pages](https://github.com/JohnPaton/johnpaton.github.io/actions/workflows/build.yml/badge.svg)](https://github.com/JohnPaton/johnpaton.github.io/actions/workflows/build.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


# johnpaton.net

This is the source repository for [johnpaton.net](https://johnpaton.net), which is built with [Pelican](https://blog.getpelican.com/), deployed with GitHub Actions, and served by [GitHub Pages](https://pages.github.com/). 

## Development

The source for building the website is located in the [`main` branch](https://github.com/JohnPaton/johnpaton.github.io/tree/ain). To get started, clone the repository and also its submodules, and install the requirements:

If you don't have `uv` installed, [install uv](https://docs.astral.sh/uv/getting-started/installation/). Then:

```bash
$ git clone --recurse-submodules git@github.com:JohnPaton/johnpaton.github.io.git
$ cd johnpaton.github.io
$ git submodule update --init --recursive
$ uv sync
```

The [settings for the Pelican build](https://docs.getpelican.com/en/3.7.1/settings.html) are in `pelicanconf.py`. All the website content is stored in the `content` directory. To make changes, edit the markdown files there or make a new one. To preview your changes, from the repository root run:

```bash
$ make html
```

The generated site will be written to the `output` directory. As an alternative to rebuilding every time, you can also run `make devserver` to start a development server at `http://localhost:8000`. Every time a change is detected in one of the source files, the output will be regenerated, so you just have to refresh the page you're working on to see the changes to the source reflected.

## Deployment

Pelican setting overrides for deployment (e.g. changing the host for generated links from `localhost:8000` to `johnpaton.net`) are stored in `publishconf.py`.

Pushes to the `main` branch will be built and deployed with the [GitHub Pages Deploy action](https://github.com/JamesIves/github-pages-deploy-action).
