import sphinx_rtd_theme
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'web-adaptive'
copyright = '2022, Kus-Kus'
author = 'Kus-Kus'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, os

sys.path.append(os.path.abspath('..'))


extensions = ['sphinx_rtd_theme', 'sphinx.ext.autodoc','sphinx.ext.napoleon', 'sphinx.ext.viewcode']
pygments_style = "sphinx"
version = '0.1.0'
html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
