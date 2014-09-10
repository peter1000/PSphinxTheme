"""
.. index:: Extensions; index_styling

==================================================================
PSphinxTheme.ext.index_styling - improves css styling for genindex
==================================================================

Overview
========
This Sphinx extension intercepts & modifies the general index data before it is rendered to html, adding some additional css
classes to help *P-SphinxTheme* (e.g. :doc:`/main_cloud_theme`) provide additional per-type styling for index entries.


Internals
=========
This extension adds the following css classes to ``genindex.html``:

- For all entries referencing an ``attribute``, ``method``, ``class``, ``function``, or ``module``:

  - The text containing the type of the entry (e.g. ``attribute`` or ``method``) is wrapped in a

   :samp:`<span class="category {type}">...</span>` tag.

  - If the entry contains a location (e.g. ``myclass in module myapp``), the ``myapp`` portion is wrapped in a

   ``<span class="location">...</span>`` tag.

- Entries which don't fit into one of the above categories are not modified.

"""
from re import (
   compile as re_compile,
)

# noinspection PyPep8Naming
from jinja2 import (
   escape,
   Markup as literal,
)


prefix = r'^(?P<name>.*)\('
suffix = r'\)$'
_attr_re = re_compile(prefix + r'(?P<left>)(?P<loc>.*)(?P<right> attribute)' + suffix)
_meth_re = re_compile(prefix + r'(?P<left>)(?P<loc>.*)(?P<right> method)' + suffix)
_fc_re = re_compile(prefix + r'(?P<left>class in |in module )(?P<loc>.*)(?P<right>)' + suffix)
_mod_re = re_compile(prefix + r'module' + suffix)


def format_index_name(name):
   """ format_index_name

   :param name:
   :return:
   """
   loc = ''
   type_ = ''
   left = ''
   right = ''
   while True:
      m = _attr_re.match(name)
      if m:
         name, left, loc, right = m.group('name', 'left', 'loc', 'right')
         type_ = 'attribute'
         break
      m = _meth_re.match(name)
      if m:
         name, left, loc, right = m.group('name', 'left', 'loc', 'right')
         type_ = 'method'
         break
      m = _fc_re.match(name)
      if m:
         name, left, loc, right = m.group('name', 'left', 'loc', 'right')
         if left.startswith('class'):
            type_ = 'class'
         else:
            type_ = 'function'
         break
      m = _mod_re.match(name)
      if m:
         name = m.group('name')
         left = 'module'
         loc = right = ''
         type_ = 'module'
         break
      return name
   if loc:
      loc = literal('<span class="location">') + escape(loc) + literal('</span>')
   cat = left + loc + right
   return escape(name) + literal('<span class="category ' + type_ + '">') + escape(cat) + literal('</span>')


# noinspection PyUnusedLocal
def mangle_index(app, pagename, templatename, ctx, event_arg):
   """ mangle_index

   :param app:
   :param pagename:
   :param templatename:
   :param ctx:
   :param event_arg:
   :return:
   """
   if pagename != 'genindex':
      return
   fmt = format_index_name
   for key, entries in ctx['genindexentries']:
      for idx, entry in enumerate(entries):
         name, (links, subitems) = entry
         entries[idx] = fmt(name), (links, subitems)
         for idx_, entry_ in enumerate(subitems):
            name, links = entry_
            subitems[idx_] = fmt(name), links


def setup(app):
   """ register extension
   """
   app.connect('html-page-context', mangle_index)
