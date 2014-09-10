"""
.. index:: Extensions; sidebarlogo_perpag

===========================================================================
PSphinxTheme.ext.sidebarlogo_perpag - override sphinx sidebar logo per-page
===========================================================================

Overview
========
This extension adds an option to set different sidebar logo per-page.


Configuration
=============
This extension reads the following ``conf.py`` options:

   ``sidebarlogo_perpage_dict``: a glob map (ala html_sidebars), used to change sidebar logo per-page

      .. important::

         - any image must be in the path: ``html_static_path``
         - do not prefix any image files with a extra path: only use the file name


      FORMAT:

         - keys: (None or image name string) e.g.: 'P-SphinxTheme180_95cloud.png'
         - value: (list or set of html pages): e.g.: ['index', 'copyright'], set({'index', 'copyright'})

For example, the following snippet uses:

   - uses a general sidebar logo: `_static/P-SphinxTheme180_95_logo.png`
   - for the *index page* and the *copyright page*: it does not use any sidebar logo
   - for the *main_cloud_theme page* and *history*: is uses the sidebar logo `_static/P-SphinxTheme180_95cloud.png`

.. index:: Usage; extension: sidebarlogo_perpag usage example

``conf.py`` Usage Example::


   # The name of an image file (relative to this directory) to place at the top of the sidebar.
   html_logo = 'P-SphinxTheme180_95_logo.png'

   # modify logo per page: using: P-Sphinx Theme extension: sidebarlogo_perpag
   sidebarlogo_perpage_dict = {
      None: set({'index', 'copyright'}),
      'P-SphinxTheme180_95cloud.png': set({'main_cloud_theme', 'history'})
   }
"""

# ===========================================================================================================================
# imports
# ===========================================================================================================================
from PSphinxTheme.utils import Err


# ===========================================================================================================================
# sphinx hooks
# ===========================================================================================================================
# noinspection PyUnusedLocal,PyUnusedLocal
def sidebarlogo_perpag_html_logo(app, pagename, templatename, ctx, event_arg):
   """ helper to override sidebar logo per-page
   """
   conf_sidebar_logo_dict = getattr(app.config, 'sidebarlogo_perpage_dict', {})
   tmp_logo = ctx.get('logo')

   found_per_page = False
   for img_key, page_name_set in conf_sidebar_logo_dict.items():
      if pagename in page_name_set:
         # check pagename in more than one set
         if found_per_page:
            raise Err('ext.sidebarlogo_perpag.sidebarlogo_perpag_html_logo()', [
               'pagename: <{}> seems to be already in an other set'.format(pagename),
               '   see: sidebarlogo_perpag_html_logo_dict: <{}>'.format(conf_sidebar_logo_dict),
            ])
         else:
            found_per_page = True
            tmp_logo = img_key

   if tmp_logo is None:
      ctx.pop('logo', None)
   else:
      ctx['logo'] = tmp_logo


# ===========================================================================================================================
# sphinx init
# ===========================================================================================================================
def setup(app):
   """ register extension
   """
   app.add_config_value('sidebarlogo_perpage_dict', None, 'env')
   app.connect('html-page-context', sidebarlogo_perpag_html_logo)

# ===========================================================================================================================
# eof
# ===========================================================================================================================
