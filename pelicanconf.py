#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date


AUTHOR = "John Paton"
SITENAME = "John Paton"
SITEURL = "http://localhost:8000"  #'http://johnpaton.github.io'
SITELOGO = "/images/headshot2.jpg"
SITE_PREVIEW_IMAGE = "/images/headshot_wide2.jpg"

TAG_GRAPH = True

FAVICON = "/images/favicon.ico"

SITETITLE = AUTHOR

_slash_left = """<b style="color:#3aa500;margin-right:2px">/</b>"""
_slash_mid = """<b style="color:#3aa500;margin-right:2px;margin-left:2px">/</b>"""
SITESUBTITLE = f"""
  <div style="width:100%;align-content:center;padding:0;">
    <div style="margin:auto 0;padding:0;display:inline-block;">
      <span style="float:left">
        {_slash_left}data{_slash_mid}scientist
      </span><br>
      <span style="float:left">
        {_slash_left}ml{_slash_mid}engineer
      </span>
    </div>
  </div>
"""

SITEDESCRIPTION = (
    "John's deep musings and cheap tricks for "
    + "Python, data science, machine learning, and more."
)

PATH = "content"

# OUTPUT_PATH = 'output/'

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

TYPOGRIFY = True
PYGMENTS_STYLE = "monokai"

BROWSER_COLOR = "#3aa500"

SUMMARY_MAX_LENGTH = 50

THEME = "themes/flex-mod"
USE_LESS = False

# GOOGLE_ANALYTICS = 'UA-92349567-1'

COPYRIGHT_YEAR = date.today().year
COPYRIGHT_NAME = "John Paton"

GITHUB_URL = "http://www.github.com/johnpaton/johnpaton.github.io"

MAIN_MENU = False

CUSTOM_CSS = "styles/custom.css"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# DISQUS_SITENAME = 'johnpatonblog'

# Blogroll
# MENU_ITEMS = [('Item 1','http://www.google.com')]


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

LINKS = (
    ("blog", "/"),
    ("tags", "/tags"),
    ("projects", "/projects"),
    ("about me", "/about"),
    ("writing&nbsp;&&nbsp;talks", "/writing-talks"),
)


# Social widget
SOCIAL = (
    ("github", "http://www.github.com/johnpaton"),
    ("twitter", "http://www.twitter.com/jd_paton"),
    ("linkedin", "http://linkedin.com/in/john-paton"),
    ("file-pdf-o", "/static/johnpaton-cv.pdf"),
    ("rss", "/feeds/all.atom.xml"),
)

# URL settings
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
DISABLE_URL_HASH = True
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DEFAULT_PAGINATION = 25

STATIC_PATHS = [
    "images",
    "styles",
    "static",
    "posts/*",
    ".well-known",
    "_config.yml",
    "images/favicon.ico",
    "CNAME",
    ".nojekyll",
]

EXTRA_PATH_METADATA = {
    "images/favicon.ico": {"path": "favicon.ico"},
}

ARTICLE_EXCLUDES = STATIC_PATHS

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Plugins
PLUGIN_PATHS = ["plugins/pelican-plugins"]
PLUGINS = ["sitemap", "render_math", "post_stats", "deadlinks"]

DEADLINK_VALIDATE = True

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.6},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.do"]}

# MATH_JAX = {'responsive':True,'linebreak_automatic':True}
MATH_JAX = {
    "source": "'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML'"
}
