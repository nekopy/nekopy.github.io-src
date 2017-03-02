# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'neko.py'
SITENAME = u'stderr'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)
         

# Social widget
SOCIAL = (('Bakabot Discord', 'https://discord.gg/Baka'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


## custom
MARKDOWN = True

THEME='eevee'
THEME_PRIMARY='blue_grey'
THEME_ACCENT='indigo'

MENUITEMS = (('Profile', 'https://github.com/nekopy'),)
