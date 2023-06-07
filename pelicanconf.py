# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alberto Verga'
SITENAME = 'Random physics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# VERGA
# content tree
STATIC_PATHS = [ 'images', 
        'pdfs', 
        'extras',
        ]
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'rphys.png'},
}
#
# theme
THEME = 'themes/alv'
PYGMENTS_STYLE = 'autumn'
HIDE_AUTHORS = True
SITESUBTITLE = 'Alberto Verga, research notebook'
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = ( ('Blog', '/'), )

TYPOGRIFY = True

# maths
MATH_JAX = {
        'linebreak_automatic': True,
        'responsive': True, 
        'responsive_align': True,
        'responsive_break': 700,
        'equation_numbering': "AMS"}
# markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
    },
    'output_format': 'html5',
}

