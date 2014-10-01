"""
.. index:: Extensions; escaped_samp_literals

======================================
PSphinxTheme.ext.escaped_samp_literals
======================================

Overview
========
**permits escaped bracket characters in "samp" role**

This extension modifies how ``:samp:`` literals are parsed, replacing the default Sphinx parser with an alternate one that
allows embedding literal ``{`` and ``}`` characters within the content, as well providing stricter input validation.


.. index:: Literals; escaped_samp_literals usage example, Usage; extension: escaped_samp_literals usage example

.. important:: To embed a literal ``{``

   **within normal docs** just use a `double-backslash` to escape it

   **within docstrings** one needs `triple-backslash` to escape it


... using `triple-backslash` to escape it and it will be rendered as:

   :samp:`this is a {variable}, these are a literal \\\{ and \\\}`


Internals
=========
.. note::

   This feature has been submitted to the Sphinx
   `issue tracker <http://bitbucket.org/birkenfeld/sphinx/issue/789/samp-text-role-lacks-ability-to-escape>`_.
   If and when the patch is accepted (or an alternative is added to Sphinx), this extension will be deprecated and eventually
   removed.

"""
from docutils import nodes, utils


# noinspection PyUnusedLocal,PyDefaultArgument
def emph_literal_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
   """ replacement for sphinx's ``:samp:`` role handler.
   this is a bit stricter in it's parsing, and allows escaping of literal
   ``{`` and ``}`` characters.
   """

   def make_error(pos, value):
      """ make_error

      :param pos:
      :param value:
      :return:
      """
      value = "%s at char %d of %s" % (value, pos, rawtext)
      msg = inliner.reporter.error(value, line=lineno)
      prb = inliner.problematic(rawtext, rawtext, msg)
      return [prb], [msg]

   text = utils.unescape(text)
   retnode = nodes.literal(role=typ.lower(), classes=[typ])
   buffer = ''  # contains text being accumulated for next node
   in_escape = False  # True if next char is part of escape sequence
   in_var = False  # True if parsing variable section instead of plain text
   var_start = None  # marks start of var section if in_var is True
   i_ = 0
   for char_ in text:
      i_ += 1
      if in_escape:
         # parse escape sequence
         if char_ in '{}\\':
            buffer += char_
            in_escape = False
         else:
            return make_error(i_ - 2, "unknown samp-escape '\\\\%s'" % (char_,))
      elif char_ == '\\':
         # begin escape sequence
         in_escape = True
         i_ += 1  # account for extra escape char in rawtext
      elif in_var:
         # parsing variable section
         if char_ == '{':
            return make_error(i_, "unescaped '{'")
         elif char_ == '}':
            # finalize variable section, return to plaintext
            if not buffer:
               return make_error(i_ - 1, 'empty variable section')
            retnode += nodes.emphasis(buffer, buffer)
            buffer = ''
            in_var = False
         else:
            buffer += char_
      else:
         # parsing plaintext section
         if char_ == '{':
            # finalize plaintext section, start variable section
            if buffer:
               retnode += nodes.Text(buffer, buffer)
            buffer = ''
            in_var = True
            var_start = i_
         elif char_ == '}':
            return make_error(i_, "unescaped '}'")
         else:
            buffer += char_
   if in_escape:
      return make_error(i_, "unterminated samp-escape sequence")
   elif in_var:
      return make_error(var_start, "unterminated variable section")
   elif buffer:
      retnode += nodes.Text(buffer, buffer)
   return [retnode], []


# noinspection PyUnusedLocal
def setup(app):
   """ register extension
   """
   # register our handler to override sphinx.roles.emph_literal_role
   from docutils.parsers.rst import roles
   import sphinx.roles as mod

   names = [
      key for key, value in mod.specific_docroles.items()
      if value is mod.emph_literal_role
   ]
   for name in names:
      roles.register_local_role(name, emph_literal_role)
