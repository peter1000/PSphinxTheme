"""
.. index:: Extensions; table_styling

==============================
PSphinxTheme.ext.table_styling
==============================

Overview
========
**adds directives for styling tables**

This Sphinx extension replaces the default ``.. table::`` directive with a custom one, that supports a number of extra
options for controlling table layout on a per-column basis.

.. index:: Tables; table_styling Table examples, Usage; extension: table_styling usage example

For example, the following snippet specifies relative widths for the three columns, changes the text alignment for each
column, disables text-wrapping for the third column, and inserts dividers between the columns::

   .. table:: Optional Caption
      :widths: 3 2 1
      :column-alignment: left center right
      :column-wrapping: true true false
      :column-dividers: none single double single

      =========== =========== ===========
      Width 50%   Width 33%   Width 16%
      =========== =========== ===========
      Line 1      This text   This text
                  should wrap will always
                  onto        be one line.
                  multiple
                  lines.
      Line 2      Centered.   Right-Aligned.
      Line 3      Centered    Right-Aligned
                  Again.      Again.
      =========== =========== ===========

This will then result in the following table:

.. table:: Optional Caption
   :widths: 3 2 1
   :column-alignment: left center right
   :column-wrapping: yes yes no
   :column-dividers: none single double single

   =========== =========== ===========
   Width 50%   Width 33%   Width 16%
   =========== =========== ===========
   Line 1      This text   This text
               should wrap will always
               onto        be one line.
               multiple
               lines.
   Line 2      Centered.   Right-Aligned.
   Line 3      Centered    Right-Aligned
               Again.      Again.
   =========== =========== ===========


Directive Options
=================
The enhanced ``.. table::`` directive supports the following options:

``:widths:``
   Sets proportional column widths

   This should be a space-separated list of positive integers, one for every column. The columns widths will be allocated
   proportionally (e.g. ``1 2 3`` for a 3-column table means the columns will use 16%, 33%, and 50% of the total width,
   respectively).

``:column-alignment:``
   Sets per-column text alignment

   This should be a comma/space-separated list of the following strings: ``left``, ``right``, ``center``, ``justify``.
   These are interpreted one per column. Extra values are ignored; if not enough values are provided, the remaining columns
   will default to ``left``.

   Alternately this can be a single word containing just the first letters: e.g. ``lrcj`` would be interpreted the same as
   ``left right center justify``.

``:column-wrapping:``
   Sets per-column text wrapping

   This should be a comma/space-separated list of either ``yes``/``true`` or ``no``/``false``. If ``yes`` (the default),
   words will wrap around if there is not enough horizontal space. If ``no``, whitespace-wrapping will be disabled for that
   column. Extra values are ignored; if not enough values are provided, the remaining columns will default to ``true``.

   Alternately this can be a single word containing just the first letters: e.g. ``ttf`` is the same as ``true true false``.

``:column-dividers:``
   Add dividers between columns

   This lets you specify custom vertical dividers between columns (ala what ``.. tabularcolumns::`` allows under latex).

   This should be a comma/space-separated list of ``none``, ``single``, or ``double``; based on the type of divider you want.
   There should be one of these for the left side of the table, for between each column, and for the right side of the table
   (e.g. a 4 entries for a 3-column table). Extra values are ignored; if not enough values are provided, the remaining
   columns will default to ``none``.

   Alternately this can be a single word containing just the number: e.g. ``0121`` is the same as
   ``none single double single``.

``:column-classes:``
   Add per-column css classes.

   This lets you specify css classes that will be assigned to each column, much like ``.. rst-class::``. This should either
   be a space-separated list containing one class per column, or a comma-separated list containing multiple classes for each
   column, separated by spaces. Extra values are ignored; if there are not enough values, or there are blank entries, those
   columns will not be assigned any custom classes.

   For example, ``a b, c , , d`` would assign the classes ``a b`` to column 1, ``c`` to column 2, no custom classes for
   column 3, and ``d`` to column 4.

``:header-columns:``
   Specify number of "stub" columns

   Should be a non-negative integer specifying the number of columns (starting with the left side) that should be treated as
   "stub" or "header" columns, and should be styled accordingly.


Internals
=========
By default, all HTML tables styled by this extension will have the css class ``"styled-table"`` added, to help with themeing
support. Use this option to override with your own theme's preferred css class.

.. note::

   This extension gets the job done by adding custom css classes to every cell in the generated html table. It then inserts a
   custom css file which provides styling implementing relevant parts of the above directives. While this extension is
   primarily tested with :mod:`!PSphinxTheme`, it should work with most Sphinx themes, any conflicts that occur are probably
   bugs.

.. todo:: allow ``:widths:`` to support ``em``, ``in``, ``%``

"""
from itertools import zip_longest

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import RSTTable


__all__ = ['setup', ]


# ===========================================================================================================================
# field option parsers
# ===========================================================================================================================
def _parse_argument_map(argument, argmap, param):
   """ Helper: _parse_argument_map
   """
   if ',' in argument:
      args = argument.split(',')
   else:
      args = argument.split()
   if len(args) == 1 and all(c in argmap for c in args[0]):
      args = args[0]

   def norm(arg):
      try:
         return argmap[arg]
      except KeyError:
         raise ValueError('invalid %s: %r' % (param, arg))

   return [norm(arg) for arg in args]


_alignment_map = dict(
   l='left',
   r='right',
   c='center',
   j='justify',
   left='left',
   right='right',
   center='center',
   centered='center',  # compat alias
   justify='justify',
   justified='justify',  # compat alias
)


def alignment_list(argument):
   """ convert into list of alignment options.
   raise ``ValueError`` if no args found, or invalid strings.
   """
   return _parse_argument_map(argument, _alignment_map, 'alignment')


_bool_map = {
   'true': True,
   't': True,
   'yes': True,
   'y': True,
   'false': False,
   'f': False,
   'no': False,
   'n': False,
}


def bool_list(argument):
   """ convert to list of true/false values
   """
   return _parse_argument_map(argument, _bool_map, 'boolean value')


def class_option_list(argument):
   """ convert to list of list of classes
   """
   if ',' in argument:
      args = argument.split(',')
   else:
      args = argument.split()
   return [directives.class_option(arg) for arg in args]


_divider_map = {
   '0': 'no',
   '1': 'single',
   '2': 'double',
   'none': 'no',
   'single': 'single',
   'double': 'double',
}


def divider_list(argument):
   return _parse_argument_map(argument, _divider_map, 'divider style')


# ===========================================================================================================================
# replacement for table directive
# ===========================================================================================================================
class ExtendedRSTTable(RSTTable):
   option_spec = RSTTable.option_spec.copy()
   option_spec.update({
      # class, name already present
      # 'header-rows': directives.nonnegative_int,
      'header-columns': directives.nonnegative_int,
      # TODO: column-widths: support limited set of units (em/in/%)
      # expressible under both css & latex
      'widths': directives.positive_int_list,
      'column-alignment': alignment_list,
      'column-wrapping': bool_list,
      'column-classes': class_option_list,
      'column-dividers': divider_list,
   })

   def run(self):
      """ run
      """
      result = RSTTable.run(self)
      if result and isinstance(result[0], nodes.table):
         self._update_table_classes(result[0])
      return result

   def _update_table_classes(self, table):
      """ _update_table_classes
      """
      assert isinstance(table, nodes.table)
      table['classes'].append('styled-table')
      header_cols = self.options.get('header-columns') or 0
      # header_rows = self.options.get('header-rows')
      widths = self.options.get('widths')
      dividers = self.options.get('column-dividers')
      if dividers is None:
         get_divider = None
      else:
         def get_divider(idx_):
            try:
               return dividers[idx_]
            except IndexError:
               return 'no'
      # noinspection PyPep8Naming
      EMPTY = ()
      opts = (
         self.options.get('column-alignment', EMPTY),
         self.options.get('column-wrapping', EMPTY),
         self.options.get('column-classes', EMPTY),
      )

      # noinspection PyShadowingNames
      def locate(cls):
         """ Helper: locate
         """
         for child_ in table.children:
            if isinstance(child_, cls):
               return child_
         return None

      tgroup = locate(nodes.tgroup)
      if not tgroup:
         return
      col = 0
      for child in tgroup:
         if isinstance(child, nodes.colspec):
            if widths and col < len(widths):
               child['colwidth'] = widths[col]
            if col < header_cols:
               child['stub'] = 1
            col += 1
            continue
         assert isinstance(child, (nodes.thead, nodes.tbody))
         for row in child.children:
            # add alignment and wrap classes to each entry
            # (would add to colspec, but html doesn't inherit much from colgroup)
            assert isinstance(row, nodes.row)
            for idx, (entry, align, wrap, clist) in enumerate(zip_longest(row, *opts)):
               if entry is None:
                  raise ValueError('not enough columns for field options')
               assert isinstance(entry, nodes.entry)
               classes = entry['classes']
               if align:
                  classes.append(align + '-align')
               if wrap is False:
                  classes.append('nowrap')
               if clist:
                  classes.extend(clist)
               if get_divider:
                  # noinspection PyCallingNonCallable
                  classes.append(get_divider(idx) + '-left-divider')
                  # noinspection PyCallingNonCallable
                  classes.append(get_divider(idx + 1) + '-right-divider')


# ===========================================================================================================================
# register extension
# ===========================================================================================================================
def setup(app):
   """ register extension
   """
   # replace existing table directive with custom one
   app.add_directive('table', ExtendedRSTTable)

# ===========================================================================================================================
# eof
# ===========================================================================================================================
