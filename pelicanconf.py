# Pelican Configuration File for Development Environment
# This file contains all the settings for the Pelican static site generator
# Used during development and local testing

# Site Information
AUTHOR = 'Helen'                    # Author name displayed on the site
SITENAME = 'Life Is Real.'          # Site title shown in browser and templates
SITEURL = ""                        # Base URL of the site (empty for local development)

# Content Configuration
PATH = "content"                    # Directory containing the site content (Markdown files)

# Regional Settings
TIMEZONE = 'Asia/Shanghai'          # Timezone for date/time formatting
DEFAULT_LANG = 'en'  # Default language for the site

# Feed Generation Settings
# RSS/Atom feeds are typically disabled during development
FEED_ALL_ATOM = None               # Disable main atom feed
CATEGORY_FEED_ATOM = None          # Disable category atom feeds
TRANSLATION_FEED_ATOM = None       # Disable translation atom feeds
AUTHOR_FEED_ATOM = None            # Disable author atom feeds
AUTHOR_FEED_RSS = None             # Disable author RSS feeds

# Blogroll - Links to display in the sidebar
LINKS = (
    ("Pelican", "https://getpelican.com/"),  # Link to Pelican documentation
)

# Social Media and External Links
GITHUB_URL = "https://github.com/liujuanjuan1984/liujuanjuan1984.github.io"  # GitHub repository URL

# Pagination Settings
DEFAULT_PAGINATION = 20            # Number of articles per page

# URL Configuration
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True             # Enable relative URLs for local development

# Theme Configuration
THEME = 'pelican-themes/clean-blog'  # Path to the theme directory

# Content Display Settings
# Control the length of the summary of the article
SUMMARY_MAX_LENGTH = 1200          # Maximum characters for article summaries

# Related Posts Plugin Settings
RELATED_POSTS_MAX = 5              # Maximum number of related posts to show
RELATED_POSTS_SKIP_SAME_CATEGORY = False  # Whether to skip posts from same category

# Static Files Configuration
# Files and directories to copy to the output directory without processing
STATIC_PATHS = [
    'images',                      # Copy images directory
    'favicon.ico',                 # Copy favicon
    'logo.png',                    # Copy logo image
    '.htaccess',                   # Copy Apache configuration
    'robots.txt'                   # Copy robots.txt for SEO
]


