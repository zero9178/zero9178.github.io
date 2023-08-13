# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import hashlib

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Personal Website'
copyright = '2023, Markus Böck'
author = 'Markus Böck'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "ablog",
    "sphinx_design",
]

myst_enable_extensions = ['dollarmath']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', '.idea', '.github']

# Blog options

blog_baseurl = "https://zero9178.github.io/"
blog_title = "My blog"
blog_path = "blog"
blog_post_pattern = "blog/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Talking about Compilers, MLIR, LLVM and C++"
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

blog_languages = {
    'en': ('English', None),
}
blog_authors = {
    'Markus Böck': ('Markus Böck', blog_baseurl + "/aboutme.html"),
}
blog_default_author = "Markus Böck"
blog_default_language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search this site...",
    "icon_links": [
        {
            "name": "EMail",
            "url": "mailto:markus.boeck02@gmail.com",
            "icon": "fa fa-envelope",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/zero9178/",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Discord",
            "url": "https://discordapp.com/users/232218093730922496",
            "icon": "fa-brands fa-discord",
        }
    ],
}

html_static_path = ['_static']

my_email = b"markus.boeck02@gmail.com"

html_logo = f"https://www.gravatar.com/avatar/{hashlib.md5(my_email).hexdigest()}?s=200"
html_favicon = f"https://www.gravatar.com/avatar/{hashlib.md5(my_email).hexdigest()}?s=32"
html_title = "zero9178"
html_sidebars = {
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
    "index": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
}
