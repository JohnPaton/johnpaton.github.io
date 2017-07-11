#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# to do: get rid of /output/ in URL, make about me (and other) pages

AUTHOR = 'John Paton'
SITENAME = "John's Blog"
SITEURL = 'http://localhost:8000'#'http://johnpaton.github.io'
SITELOGO = '/images/headshot.jpg'
FAVICON = '/images/favicon.ico'

SITETITLE = AUTHOR
SITESUBTITLE = 'data scientist'+\
               '<b style="color:#3aa500;font-size:20px;word-spacing:0px"> | </b>'+\
               'consultant'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'English'

#TYPOGRIFY = True
PYGMENTS_STYLE = 'monokai'

BROWSER_COLOR = '#3aa500'

SUMMARY_MAX_LENGTH = 50

THEME = 'themes/flex-mod'
USE_LESS = False

GOOGLE_ANALYTICS = 'UA-92349567-1'

COPYRIGHT_YEAR = 2017
COPYRIGHT_NAME = 'John Paton'

GITHUB_URL = 'http://www.github.com/johnpaton/johnpaton.github.io'

MAIN_MENU = False


#EXTRA_PATH_METADATA = {
#    'styles/custom.css': {'path': 'static/custom.css'},
#}

CUSTOM_CSS = '/styles/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'johnpatonblog'

# Blogroll
# MENU_ITEMS = [('Item 1','http://www.google.com')]


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

LINKS = (('about me', '/pages/about'),
         ('tags', '/tags'),
         )


# Social widget
SOCIAL = (('github', 'http://www.github.com/johnpaton'),
          ('twitter', 'http://www.twitter.com/jd_paton'),
          ('linkedin', 'http://linkedin.johnpaton.net'),
          ('rss', '/feeds/all.atom.xml')
          )

# URL settings
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
DISABLE_URL_HASH = True
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images','styles']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS=['sitemap', 'render_math']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.6
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
