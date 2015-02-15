import sys, os.path
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxarg.ext'
]

source_suffix = '.rst'
master_doc = 'index'

project = 'bong'
copyright = '2015, Alistair Lynn'

from bong.metadata import VERSION as version
release = version

html_theme = 'default'

