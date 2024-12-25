import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'AIge of EmpAIres'
copyright = '2024, KRILL Maxence, MUNT-BURON Killian, NGUYEN Dinh Huy, NGUYEN Nhat Lam, OUSEGGUA Mehdi, STOLL Nicolas'
author = 'KRILL Maxence, MUNT-BURON Killian, NGUYEN Dinh Huy, NGUYEN Nhat Lam, OUSEGGUA Mehdi, STOLL Nicolas'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']