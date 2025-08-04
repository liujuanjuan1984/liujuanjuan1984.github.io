# Pelican Configuration File for Production Environment
# This file is only used if you use `make publish` or explicitly specify it as your config file.
# Contains production-specific settings that override development settings

import os
import sys

# Add current directory to Python path to import pelicanconf
sys.path.append(os.curdir)
from pelicanconf import *

# Site URL Configuration for Production
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://liujuanjuan1984.github.io"                        # Production site URL (set to actual domain when deployed)
RELATIVE_URLS = False               # Use absolute URLs in production

# Feed Generation for Production
# Enable RSS/Atom feeds for production to improve site discoverability
FEED_DOMAIN = SITEURL                           # Domain for feed URLs
FEED_ALL_ATOM = "feeds/all.atom.xml"           # Main atom feed for all articles
# Disable category feeds for now to avoid template formatting issues
CATEGORY_FEED_ATOM = None                       # Disable category atom feeds

# Output Directory Management
DELETE_OUTPUT_DIRECTORY = True      # Clean output directory before each build

# Following items are often useful when publishing
# Uncomment and configure these services as needed

# Disqus Comments Integration
# DISQUS_SITENAME = ""             # Your Disqus shortname for comments

# Google Analytics Integration
# GOOGLE_ANALYTICS = ""            # Your Google Analytics tracking ID
