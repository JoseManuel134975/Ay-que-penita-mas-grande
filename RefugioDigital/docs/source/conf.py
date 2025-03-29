# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

sys.path.insert(0, os.path.abspath('../../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'RefugioDigital.settings'
django.setup()

project = 'RefugioDigital'
copyright = '2025, Jose Manuel Martinez Fernandez, Alejandro Polo Barranco, Andres Nenis Pinilla, Gabriel Gomez Rodriguez'
author = 'Jose Manuel Martinez Fernandez, Alejandro Polo Barranco, Andres Nenis Pinilla, Gabriel Gomez Rodriguez'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Configuración adicional para autodoc
autodoc_default_options = {
    'members': True,       # Incluir todos los miembros (funciones, métodos)
    'undoc-members': True, # Incluir miembros sin docstrings
    'show-inheritance': True, # Mostrar la jerarquía de herencia
}

# Para dar soporte a estilo de docstrings Google o NumPy
napoleon_google_docstring = True  # Para Google-style docstrings
napoleon_numpy_docstring = True   # Para NumPy-style docstrings
