# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Introduction to Geodynamic Modelling'
copyright = '2017-2024, David Whipp and Lars Kaislaniemi, University of Helsinki'
author = ''
version = '2024'
release = '2024'

# -- General configuration

extensions = [
    "myst_nb",
    "sphinx.ext.viewcode",
    #"sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_thebe",
    "sphinx_togglebutton",
    #"sphinxcontrib.bibtex",
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sphinx_book_theme"
html_logo = "img/introgm-logo.png"
html_title = ""
html_copy_source = True
html_sourcelink_suffix = ""
#html_favicon = "_static/logo-square.svg"
html_last_updated_fmt = ""

#html_sidebars = {
#    "reference/blog/*": [
#        "sidebar-logo.html",
#        "search-field.html",
#        "postcard.html",
#        "recentposts.html",
#        "tagcloud.html",
#        "categories.html",
#        "archives.html",
#        "sbt-sidebar-nav.html",
#    ]
#}

html_theme_options = {
    "path_to_docs": "docs/source",
    "repository_url": "https://github.com/IntroGM/site",
    # "repository_branch": "gh-pages",  # For testing
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        #"colab_url": "https://colab.research.google.com/",
        #"deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "logo_only": True,
    "show_toc_level": 2,
    # For testing
    # "use_fullscreen_button": False,
    # "home_page_in_toc": True,
    # "single_page": True,
    # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
    # "extra_navbar": "<a href='https://google.com'>Test</a>",
    # "show_navbar_depth": 2,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable auto-generated header anchors
myst_heading_anchors = 3

