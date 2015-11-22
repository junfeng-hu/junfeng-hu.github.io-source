#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'junfeng'
SITENAME = 'jf.h'
SITEURL = ''
SITESUBTITLE = 'lylx'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# menuitems
MENUITEMS = (
        (u'首页', u'/'),
        )
# Blogroll
LINKS =  (
          )

# Social widget
SOCIAL = (
        ('GitHub', 'https://github.com/junfeng-hu'),
        ('Bitbucket', 'https://bitbucket.org/junfeng_hu'),
        ('Twitter', 'https://twitter.com/junfeng_hu'),
        ('Weibo', 'http://weibo.com/junfeng7'),
        ('Instagram', 'http://instagram.com/junfeng_hu'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "fresh"

PLUGIN_PATHS = [".",
        ]
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}


DEFAULT_CATEGORY = u"Python"

ARCHIVES_URL = "archives.html"

# GITHUB_URL = u"https://github.com/junfeng-hu"
 #GITHUB_POSITION = "right"

STATIC_PATHS = ["images",
                "static/upload",
                "extra/favicon.ico",
                #"extra/robots.txt",
                #"extra/bdsitemap.txt",
                #"extra/404.html",
                ]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    #"extra/robots.txt": {"path": "robots.txt"},
    #"extra/bdsitemap.txt": {"path": "bdsitemap.txt"},
    #"extra/404.html": {"path": "404.html"},
}



HIDE_CATEGORIES_FROM_MENU = True
