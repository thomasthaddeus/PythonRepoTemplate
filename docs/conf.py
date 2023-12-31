# conf.py

# -- Project information -----------------------------------------------------

project = 'My Documentation'
author = 'Your Name'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For parsing Google-style docstrings
]

# Add any other settings or customizations as needed

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # Use the ReadTheDocs theme (install it separately)
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # Add LaTeX-specific settings here
}

# Additional configuration options can be added based on your needs
