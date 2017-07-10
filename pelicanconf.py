#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# to do: get rid of /output/ in URL, make about me (and other) pages

AUTHOR = 'John Paton'
SITENAME = "John's Blog"
SITEURL = 'http://localhost:8000'#'http://johnpaton.github.io'
SITELOGO = '/content/images/headshot.jpg'
FAVICON = '/content/images/favicon.ico'

SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist <strong style="color:#3aa500;font-size:18px">|</strong> Consultant'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'English'

#TYPOGRIFY = True
PYGMENTS_STYLE = 'monokai'

BROWSER_COLOR = '#333'

SUMMARY_MAX_LENGTH = 50

THEME = 'themes/flex-mod'
USE_LESS = False

GOOGLE_ANALYTICS = 'UA-92349567-1'

COPYRIGHT_YEAR = 2017
COPYRIGHT_NAME = 'John Paton'

GITHUB_URL = 'http://www.github.com/johnpaton/johnpaton.github.io'

MAIN_MENU = False


EXTRA_PATH_METADATA = {
    'styles/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'johnpatonblog'

# Blogroll
# MENU_ITEMS = [('Item 1','http://www.google.com')]

LINKS = (('about me', SITEURL+'/author'),
         ('tags', SITEURL+'/tags'),
         )


# Social widget
SOCIAL = (('github', 'http://www.github.com/johnpaton'),
          ('twitter', 'http://www.twitter.com/jd_paton'),
          ('linkedin', 'http://linkedin.johnpaton.net'),
          )

# URL settings
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
DISABLE_URL_HASH = True
##PAGE_URL = 'pages/{slug}/'
##PAGE_SAVE_AS = 'pages/{slug}/index.html'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['styles','images']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
