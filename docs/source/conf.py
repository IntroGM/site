# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Introduction to Geodynamic Modelling'
copyright = '2017-2024, David Whipp, Lars Kaislaniemi, and Leevi Tuikka, University of Helsinki'
author = ''
version = '2024'
release = '2024'

# -- General configuration

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_thebe",
    "sphinx.ext.viewcode",
    "sphinxcontrib.youtube",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "jupyter_sphinx",
    #"sphinx_design",
    #"sphinx_tabs.tabs",
    #"sphinx_togglebutton",
    #"sphinxcontrib.bibtex",
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sphinx_book_theme"
html_logo = "img/introgm-logo-2024.png"
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

html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    "display_github": True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    "github_user": "introgm",
    "github_repo": "site",
    "github_version": "main/",
    "conf_py_path": "/docs/source/",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable auto-generated header anchors
myst_heading_anchors = 3

# -- Extension configuration -------------------------------------------------
# Allow errors when parsing pages using nbsphinx
nbsphinx_allow_errors = True

# Execute cells only if any of the cells is missing output
jupyter_execute_notebooks = "auto"

# Add math config options for new version of MyST
myst_enable_extensions = ["dollarmath"]

