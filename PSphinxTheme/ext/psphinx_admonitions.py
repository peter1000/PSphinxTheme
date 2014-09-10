# (c) 2014 `peter1000` https://github.com/peter1000
# All Rights Reserved

"""
.. index:: Extensions; psphinx_admonitions

=============================================================================
PSphinxTheme.ext.psphinx_admonitions - all official P-SphinxTheme admonitions
=============================================================================

Overview
========
This Sphinx extension is a collection of all *official P-SphinxTheme admonitions*


.. index:: Admonitions; admonitions usage example, Usage; extension: psphinx_admonitions usage example

For example, the following snippet specifies a simple `python-example admonition`::

   .. python-example:: Simple Example

      .. code-block:: python

         for key in mydict:
            print(key)

depending on other options it renders to:

.. python-example:: Simple Example

   .. code-block:: python

      for key in mydict:
         print(key)


The next example has at **the left side** a hide show prompt toggle::

   if a *code-block* starts with ``>>>`` there is an extra option on the left side to hide it

   .. python-example:: Simple Example

      .. code-block:: python

         >>> mylist = ['red', 'blue', 'green']
         >>> print(mylist[2])
         green
         >>>

it renders to:

.. python-example:: Simple Example

   .. code-block:: python

      >>> mylist = ['red', 'blue', 'green']
      >>> print(mylist[2])
      green
      >>>


Directive Admonition  Options
=============================
Adds / overwrites following options:


Replaces some *docutils* Admonitions
------------------------------------

``.. note::``

``.. tip::``

``.. note::``

``.. important::``

``.. warning::``


Replaces some *sphinx* Admonitions
----------------------------------

``.. seealso::``


Adds *additional* Admonitions
-----------------------------

``.. optional::``

``.. example::``

``.. python-example::``

``.. shell-example::``

``.. javascript-example::``

``.. json-example::``

``.. lconf-example::``


Related Options
===============

There are a couple of related theme options.

.. seealso:: :ref:`Admonitions & deprecated / todo <admonitions_deprecated_todo>`

"""
# ===========================================================================================================================
# imports
# ===========================================================================================================================
from docutils import nodes

from sphinx.util.compat import (
   Directive,
   make_admonition,
)


class PSphinxAdmonition(Directive):
   """ Admonitions for the P-SphinxTheme.
   """
   node_class = None
   label = ''

   required_arguments = 0
   optional_arguments = 1
   has_content = True
   final_argument_whitespace = True
   option_spec = {}

   def run(self):
      # noinspection PyUnresolvedReferences
      """ run
      :return:
      """
      ret = make_admonition(
         self.node_class,
         self.name,
         [self.label],
         self.options,
         self.content,
         self.lineno,
         self.content_offset,
         self.block_text,
         self.state,
         self.state_machine
      )

      if self.arguments:
         argnodes, msgs = self.state.inline_text(self.arguments[0], self.lineno)
         para = nodes.paragraph()
         para += argnodes
         para += msgs
         ret[0].insert(1, para)

      return ret


def visit_psphinx_node(self, node):
   """ visit_psphinx_node

   :param self:
   :param node:
   """
   self.visit_admonition(node)


def depart_psphinx_node(self, node):
   """ depart_psphinx_node

   :param self:
   :param node:
   """
   self.depart_admonition(node)


def _psphinx_app_setup_helper(app, name_str, node_class, admonition_class):
   """ _psphinx_app_setup_helper

   :param app:
   :param name_str:
   :param node_class:
   :param admonition_class:
   """
   app.add_node(
      node_class,
      html=(visit_psphinx_node, depart_psphinx_node),
      latex=(visit_psphinx_node, depart_psphinx_node),
      text=(visit_psphinx_node, depart_psphinx_node),
      man=(visit_psphinx_node, depart_psphinx_node),
      texinfo=(visit_psphinx_node, depart_psphinx_node)
   )

   app.add_directive(name_str, admonition_class)


# ===========================================================================================================================
# All "official" P-SphinxTheme admonitions
# ===========================================================================================================================
class NoteNode(nodes.Admonition, nodes.Element):
   """ NoteNode
   """
   pass


class TipNode(nodes.Admonition, nodes.Element):
   """ TipNode
   """
   pass


class ImportantNode(nodes.Admonition, nodes.Element):
   """ ImportantNode
   """
   pass


class WarningNode(nodes.Admonition, nodes.Element):
   """ WarningNode
   """
   pass


class SeeAlsoNode(nodes.Admonition, nodes.Element):
   """ SeeAlsoNode
   """
   pass


class OptionalNode(nodes.Admonition, nodes.Element):
   """ OptionalNode
   """
   pass


class ExampleNode(nodes.Admonition, nodes.Element):
   """ ExampleNode
   """
   pass


class PythonExampleNode(nodes.Admonition, nodes.Element):
   """ PythonExampleNode
   """
   pass


class ShellExampleNode(nodes.Admonition, nodes.Element):
   """ ShellExampleNode
   """
   pass


class JavaScriptExampleNode(nodes.Admonition, nodes.Element):
   """ JavaScriptExampleNode
   """
   pass


class JsonExampleNode(nodes.Admonition, nodes.Element):
   """ JsonExampleNode
   """
   pass


class LconfExampleNode(nodes.Admonition, nodes.Element):
   """ LconfExampleNode
   """
   pass


# # #
class NoteAdmonition(PSphinxAdmonition):
   """ NoteAdmonition
   """
   node_class = NoteNode
   label = 'Note'


class TipAdmonition(PSphinxAdmonition):
   """ TipAdmonition
   """
   node_class = TipNode
   label = 'Tip'


class ImportantAdmonition(PSphinxAdmonition):
   """ ImportantAdmonition
   """
   node_class = ImportantNode
   label = 'Important'


class WarningAdmonition(PSphinxAdmonition):
   """ WarningAdmonition
   """
   node_class = WarningNode
   label = 'Warning'


class SeeAlsoAdmonition(PSphinxAdmonition):
   """ SeeAlsoAdmonition
   """
   node_class = SeeAlsoNode
   label = 'SeeAlso'


class OptionalAdmonition(PSphinxAdmonition):
   """ OptionalAdmonition
   """
   node_class = OptionalNode
   label = 'Optional'


class ExampleAdmonition(PSphinxAdmonition):
   """ ExampleAdmonition
   """
   node_class = ExampleNode
   label = 'Example'


class PythonExampleAdmonition(PSphinxAdmonition):
   """ PythonExampleAdmonition
   """
   node_class = PythonExampleNode
   label = 'Python-Example'


class ShellExampleAdmonition(PSphinxAdmonition):
   """ ShellExampleAdmonition
   """
   node_class = ShellExampleNode
   label = 'Shell-Example'


class JavaScriptExampleAdmonition(PSphinxAdmonition):
   """ JavaScriptExampleAdmonition
   """
   node_class = JavaScriptExampleNode
   label = 'JavaScript-Example'


class JsonExampleAdmonition(PSphinxAdmonition):
   """ JsonExampleAdmonition
   """
   node_class = JsonExampleNode
   label = 'Json-Example'


class LconfExampleAdmonition(PSphinxAdmonition):
   """ LconfExampleAdmonition
   """
   node_class = LconfExampleNode
   label = 'LCONF-Example'


# ===========================================================================================================================
# sphinx init
# ===========================================================================================================================
def setup(app):
   """ register extension
   """
   # replaces some docutils Admonition
   _psphinx_app_setup_helper(app, 'note', NoteNode, NoteAdmonition)
   _psphinx_app_setup_helper(app, 'tip', TipNode, TipAdmonition)
   _psphinx_app_setup_helper(app, 'important', ImportantNode, ImportantAdmonition)
   _psphinx_app_setup_helper(app, 'warning', WarningNode, WarningAdmonition)
   # replaces some sphinx Admonition
   _psphinx_app_setup_helper(app, 'seealso', SeeAlsoNode, SeeAlsoAdmonition)
   # adds additional Admonition
   _psphinx_app_setup_helper(app, 'optional', OptionalNode, OptionalAdmonition)
   _psphinx_app_setup_helper(app, 'example', ExampleNode, ExampleAdmonition)
   _psphinx_app_setup_helper(app, 'python-example', PythonExampleNode, PythonExampleAdmonition)
   _psphinx_app_setup_helper(app, 'shell-example', ShellExampleNode, ShellExampleAdmonition)
   _psphinx_app_setup_helper(app, 'javascript-example', JavaScriptExampleNode, JavaScriptExampleAdmonition)
   _psphinx_app_setup_helper(app, 'json-example', JsonExampleNode, JsonExampleAdmonition)
   _psphinx_app_setup_helper(app, 'lconf-example', LconfExampleNode, LconfExampleAdmonition)
