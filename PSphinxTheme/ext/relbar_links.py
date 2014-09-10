# Based on previous: relbar_toc.py

"""
.. index:: Extensions; relbar_links

===========================================================
PSphinxTheme.ext.relbar_links - adds link entries to relbar
===========================================================

Overview
========
This Sphinx extension automatically inserts entries into the navigation bar (relation bar - ``relbar``) at the top and
bottom of all pages.

This can be used similar to 'Quick Links' e.g. adding a 'toc' or 'api' link

Configuration
=============
This extension reads the following ``conf.py`` options:

   ``relbar_links_doc``: a list of tuples mapping: lin-names to page-names

      .. important::

         - path is entered  relative to the ``conf.py`` and no extension


For example, the following snippet inserts two links:

   - toc: mapping the 'contents' page
   - api: mapping 'api/api' page

.. index:: Usage; extension: relbar_links usage example

``conf.py`` Usage Example::

   # The api document: extension: relbar_links
   relbar_links_doc = [
      ('toc', 'contents'),
      ('api', 'api/api'),
   ]
"""


# noinspection PyUnusedLocal
def insert_api(app, pagename, templatename, ctx, event_arg):
   """ Helper: insert_api
   """
   links = ctx['rellinks']
   links_doc = getattr(app.config, 'relbar_links_doc', {})
   links_doc_names = [k_ for k_, p_ in links_doc]

   # remove any existing entries (present on some pages)
   for idx, elem in enumerate(links):
      temp_elem3 = elem[3]
      if isinstance(temp_elem3, str):
         if elem[3] in links_doc_names:
            del links[idx]

   # place any right after "next" / "previous" in the order as defined
   idx = -1
   for idx, entry in enumerate(links):
      if entry[3] in ('next', 'previous'):
         break
   else:
      idx += 1

   # insert any entry
   for name_, path_ in links_doc:
      links.insert(idx, (path_, 'Table Of Contents', 'C', name_))


def setup(app):
   """ register extension
   """
   app.add_config_value('relbar_links_doc', None, 'env')
   app.connect('html-page-context', insert_api)
