=================================
sphinx-catalystcloud-theme
=================================
Catalyst Cloud theme for Sphinx documentation

Installation
============
::

  pip install sphinx-catalystcloud-theme

Use
===
In the conf.py file of the sphinx documentation you are adding this theme to add this line:

::

  html_theme = 'sphinx_catalystcloud_theme'


This theme was based upon both the spinx_rtd_theme and the
sphinx_bootstrap_theme.

Contributing
============

Editing
-------

To change the styles of the theme, edit the 'SCSS <https://sass-lang.com/>' in: /sphinx_catalystcloud_theme/static/cloudtheme/styles.

Compile
-------

Before pushing or committing to the repo, compile the scss to css with:

::

  cd sphinx-catalystcloud-theme
  sass --watch sphinx_catalystcloud_theme/static/cloudtheme/styles:sphinx_catalystcloud_theme/static/cloudtheme/css
