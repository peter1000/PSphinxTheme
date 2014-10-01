.. index:: P-Sphinx Theme; feature test


=============================
"P-Sphinx Theme" Feature Test
=============================

This page contains examples of various features of the *P-Sphinx Theme*. It's mainly useful internally, to make sure
everything is displaying correctly.


.. index:: Literals; literals example, Examples; literals / quoted text options

Inline Text
===========
Inline literal: ``literal text``

"samp literal" with **literal variable** using the *P-Sphinx Theme extension* :mod:`~PSphinxTheme.ext.escaped_samp_literals`

.. code-block:: text

   :samp:`this is a {variable}, these are a literal \\{ and \\}`

... and it will be rendered as:

   :samp:`this is a {variable}, these are a literal \\{ and \\}``

.. important:: To embed a literal ``{``

   **within normal docs** just use a `double-backslash` to escape it

   **within docstrings** one needs `triple-backslash` to escape it


.. index:: Examples; external references / diverse options

External links are prefixed with an arrow: `<http://www.google.com>`_.

But email links are not prefixed: bob@example.com.

Issue tracker link: :issue:`1`.


.. index:: Admonitions; admonition examples

Admonition Styles
=================

.. admonition:: MyTest

   this uses the ``.. admonition:: syntax```


.. todo::

   This is a todo message.

   With some additional next on another line.


.. deprecated:: XXX This is a deprecation warning.


.. rst-class:: floater
.. note::
   This is a floating note.

|
|
|
|

.. note::
   This is a note.

.. tip::

   This is a tip.

.. important::

   This is important.

.. warning::

   This is a warning.

.. seealso::

   This is a "see also" message.

.. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`

.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. optional::

   This is optional.


.. example:: html

   .. code-block:: html

      <!DOCTYPE html>
      <html>
      <body>

      <h1>My First Heading</h1>

      <p>My first paragraph.</p>

      </body>
      </html>


.. example:: A Python code block but maybe one should use the ``python-example`` admonition instead

   .. code-block:: python3

      # for loop
      for name in names_list:
         print(name)


.. javascript-example:: requires highlighter: `javascript`

   .. code-block:: javascript

      db.inventory.find( { type: 'food' } ).hint( { type: 1 } ).explain()
      db.inventory.find( { type: 'food' } ).hint( { type: 1, name: 1 } ).explain()

   These return the statistics regarding the execution of the query
   using the respective index.


.. shell-example::  requires highlighter: `sh`

   .. code-block:: sh

      $ rm -rf *


.. json-example::  requires highlighter: `json`

   .. code-block:: json

      {
         "first": "John",
         "last": "Doe",
         "age": 39,
         "interests": [
            "Reading",
            "Mountain Biking",
            "Hacking"
         ],
         "registered": true,
         "salary": 70000,
         "sex": "M"
      }


.. lconf-example::  requires highlighter: `lconf`

   .. code-block:: lconf

      ___SECTION :: BaseEXAMPLE

      # Comment-Line: below: Main `Key :: Value Pair`
      key1value_pair :: value1
      # Comment-Line: below is a `Key :: Value Pair` with an empty value string: which is skipped
      key2value_pair ::
      key3value_pair ::
      key4value_pair :: True
      key5value_pair :: False
      key6value_pair :: None
      key7value_pair :: 1456.984
      key8value_pair :: true
      key9value_pair :: different characters # \n * | , & @  https://translate.google.com/ translate ਅਨੁਵਾਦ  翻訳する μεταφράζω


      # Comment-Line: below is a Main `Key-Value-Mapping`
      . key10value_mapping
         # Comment-Line:  Key-Value-Mapping items: are `Key :: Value Pairs`
         mapping10_key1 :: False
         mapping10_key2 :: true
         mapping10_key3 :: 123456

         # Comment-Line:  Key-Value-Mapping item: `Key :: Value-List`
         - mapping10_key4_list :: 1,2

         # Comment-Line:  Key-Value-Mapping item: `Key-Value-List`
         - mapping10_key5_list
            1
            2

         # Comment-Line:  Key-Value-Mapping item: `List-Of-Lists`
         - mapping10_key6_list |x|y|
            1,3
            2,6

         # Comment-Line:  Key-Value-Mapping item: `List-Of-Lists`
         - mapping10_key7_list |a|b|c|
            1,2.0,3
            2,4.0,6

      # Comment-Line: below is a Main `Key-Value-Mapping`
      . key11value_mapping
         # Comment-Line:  Key-Value-Mapping item: `Key :: Value Pairs`
         mapping11_key1 :: null

         # Comment-Line:  Key-Value-Mapping item: an other nested `Key-Value-Mapping`
         . mapping11_key2_mapping
            # Comment-Line:  nested Key-Value-Mapping item: `Key :: Value Pairs`
            mapping11_key2_nested_mapping_key1 :: city

            # Comment-Line:  nested Key-Value-Mapping item: `Repeated-Block-Identifier`
            * mapping11_key2_nested_mapping_key2_block_identifier

               # Comment-Line: `Block-Name1`
               sky_blue_blk_name1
                  # Comment-Line:  Block items: `Key :: Value Pairs`
                  blk_item_red :: 135
                  blk_item_green :: 206
                  blk_item_blue :: 235

               # Comment-Line: `Block-Name2`
               lavender_blk_name2
                  # Comment-Line:  Block items: `Key :: Value Pairs`
                  blk_item_red :: 230
                  blk_item_green :: 230
                  blk_item_blue :: 250

            # Comment-Line:  nested Key-Value-Mapping item: `Key :: Value Pairs`
            mapping11_key2_nested_mapping_key3 :: car

            # Comment-Line: nested Key-Value-Mapping item: `Key-Value-List`
            - mapping11_key2_nested_mapping_key4_list
               # Comment-Line: List item
               value_list_item1
               value_list_item2


      # Comment-Line: below is a Main `Key-Value-List`
      - key12list
         # Comment-Line: List item
         value_list_item1
         value_list_item2

      # Comment-Line: below is a Main `Key :: Value-List`
      - key13value_pairlist :: 123,8945,278

      # Comment-Line: below is a Main `List-Of-Lists` with 4 items: |Color Name|Red|Green|Blue|
      - key14list_of_color_tuples |Color Name|Red|Green|Blue|
         # Comment-Line: `List-Of-Lists` item lines (rows)
         forestgreen,   34,   139,  34
         brick,         156,  102,  31

      # Comment-Line: below is a Main `Key :: Value-List` with an empty list: overwriting any defaults
      - key15value_pairlist ::

      # Comment-Line: below is a Main `Key-Value-List` with an empty list: overwriting any defaults
      - key16value_pairlist

      # Comment-Line: below is a Main `List-Of-Lists` with an empty list: overwriting any defaults
      - key17value_pairlist |a|b|c|


      # Comment-Line: below: `Repeated-Block-Identifier`
      #  this will loose the order of the `Repeated Block-Names` after parsing
      #  but any library must implement an option to loop over it in order as defined in the section
      * RepeatedBlk1
         # Comment-Line: BLK_OBJ1 (Block-Name) uses all 8 possible - defined items
         BLK_OBJ1

            # Comment-Line: below Block-Item `Key-Value-Mapping` with all 4 defined items
            . MyKey1_mapping
               blk_mapping_key1 :: some text
               blk_mapping_key2 :: 12345.99
               blk_mapping_key3 :: True

               # Comment-Line:  Block-Item `Key-Value-Mapping`: an other nested `Key-Value-Mapping`
               . blk_mapping_key4
                  nested_mapping_key1 :: franz
                  # Comment-Line:  Block-Item  nested `Key-Value-Mapping` item: an other nested `Key-Value-Lists`
                  - interests
                     sport
                     reading

                  # Comment-Line:  Block-Item: an other deep nested `Repeated-Block-Identifier`
                  * Nested Repeated Block Identifier
                     # Comment-Line:  keys do not have to be a single word: below a Block-Name
                     Nested Block Name1
                        block-item_key1 :: 12345.99
                        - block-item_key2_list :: False,True,True
                        # Comment-Line:  block-item_key3_list: `List-Of-Lists`
                        - block-item_key3_list |name|height_cm|weight_kg|
                           # Comment-Line: |name|height_cm|weight_kg|
                           Tim,     178,     86
                           John,    166,   67

            MyKey2 :: 789.9
            MyKey3 :: True

            # Comment-Line:  empty `Key :: Value Pairs`
            MyKey4 ::
            - MyKey5list :: test1,test2

            # Comment-Line: Block-Item `Key :: Value-List` with Empty List
            - MyKey6list ::

            # Comment-Line: Block-Item `Key :: Value-List`
            - MyKey7list :: True,False,False,True

            MyKey8 :: some text

         # Comment-Line: BLK_OBJ2 (Block-Name) of RepeatedBlk1: uses a subset of the defined items:
         # all others will be set to default values as implemented
         #    NOTE: Blocks are only set to defaults if a Block-Name is defined
         BLK_OBJ2

            # Comment-Line: below Block-Item `Key-Value-Mapping`: only some defined items
            . MyKey1_mapping
               blk_mapping_key3 :: False

               # Comment-Line:  Block-Item `Key-Value-Mapping`: an other nested `Key-Value-Mapping`
               . blk_mapping_key4
                  nested_mapping_key1 :: julia
                  # Comment-Line:  Block-Item  nested `Key-Value-Mapping` item: an other nested `Key-Value-Lists`
                  - interests
                     golf

                  # Comment-Line:  Block-Item: an other deep nested `Repeated-Block-Identifier`
                  * Nested Repeated Block Identifier
                     # Comment-Line:  Block-Name: all values will use defaults
                     Nested Block Name1
                     # Comment-Line:  Block-Name: and defining an empty list: block-item_key2_list
                     Nested Block Name2
                        - block-item_key2_list ::
                        # Comment-Line:  block-item_key3_list: `List-Of-Lists`: to define an empty list: skip any item lines
                        - block-item_key3_list |name|height_cm|weight_kg|

            # Comment-Line: Block-Item `Key-Value-Lists`
            - MyKey7list
               True
               False
               True

         BLK_OBJ3
            # Comment-Line: below Block-Item `Key-Value-Mapping`
            . MyKey1_mapping
               blk_mapping_key1 :: who is who " ' : .. # 1,2,3 3, d $ % & * _ = == [] < > ? / \ : ; ' 12354^ @ & () { df } \\
               blk_mapping_key2 :: 5678.89
               blk_mapping_key3 :: False

            # Comment-Line:  `Key :: Value Pairs`
            MyKey4 ::
            - MyKey5list :: test1,test2

         # Comment-Line: Repeated Block-Name: will be using all default values
         #    Note: Blocks are not having any default names: so the items are skipped
         BLK_OBJ4

      ___END

.. rst-class:: floater
.. python-example:: Dict usage floater example

   .. code-block:: python3

      for key in mydict:
         print(key)

|
|
|
|
|
|

.. index:: Admonitions; topic examples

.. _topic:

Topics
------

.. topic:: Lorem ipsum

   Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
   aliqua.


.. index:: Headings; headers examples

Headings
========

.. raw:: html

   <h1>H1: Lorem ipsum dolor sit amet</h1>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

.. raw:: html

   <h2>H2: Lorem ipsum dolor sit amet</h2>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

.. raw:: html

   <h3>H3: Lorem ipsum dolor sit amet</h3>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

.. raw:: html

   <h4>H4: Lorem ipsum dolor sit amet</h4>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

.. raw:: html

   <h5>H5: Lorem ipsum dolor sit amet</h5>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

.. raw:: html

   <h6>H6: Lorem ipsum dolor sit amet</h6>

Lorem ipsum dolor sit amet, **consectetur adipisicing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. *Ut enim ad minim* veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.


.. index:: Headings; rubric examples

Rubric
------

.. rubric:: This is an example rubric


.. index:: Paragraphs; paragraphs examples

Paragraphs
==========

Duis **aute irure dolor** in *reprehenderit* in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

`Lorem ipsum`_ dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat `cupidatat`_ non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


.. _footnotes:

.. index:: Footnotes; footnotes examples

Footnotes
=========

.. target-notes::

.. _Lorem ipsum: http://www.google.com
.. _`cupidatat`: http://docutils.sourceforge.net/rst.html


.. index:: Lists; lists examples

Lists
=====

Unordered list
--------------

- Lorem ipsum
- Dolor sit amet

  - Dolor
  - Sit
  - Amet

- Consectetur adipiscing elit

Ordered list
------------

#. Lorem ipsum
#. Dolor sit amet

   #. Dolor
   #. Sit
   #. Amet

#. Consectetur adipiscing elit

Definition Lists
----------------

Lorem
    Lorem ipsum dolor sit amet.
Ipsum
    Ipsum dolor amet sit.
Dolor : classifier
    Dolor lorem ipsum.
Sit amet : classifier one : classifier two
    Sit amet consectetur adipiscing elit.


.. index:: Tables; Table examples

Table Styles
============

Normal rst Table
----------------


+----------------------+------------------------------------------------+
| Header row, column 1 | Header row, column 2                           |
+======================+================================================+
| body row 1           | Second column of row 1                         |
+----------------------+------------------------------------------------+
| body row 2           | Second column of row 2                         |
|                      |                                                |
|                      | Second line of paragraph                       |
+----------------------+------------------------------------------------+
| body row 3           | Unordered list:                                |
|                      |                                                |
|                      | * Second column of row 3                       |
|                      | * Second item in bullet list (row 3, column 2) |
+----------------------+------------------------------------------------+
| \                    | Row 4; column 1 will be empty                  |
+----------------------+------------------------------------------------+


Tables using ``table`` directive
--------------------------------

.. table:: Normal Table

   =========== =========== ===========
   Header1     Header2     Header3
   =========== =========== ===========
   Row 1       Row 1       Row 1
   Row 2       Row 2       Row 2
   Row 3       Row 3       Row 3
   =========== =========== ===========

.. rst-class:: plain

.. table:: Plain Table (no row shading)

   =========== =========== ===========
   Header1     Header2     Header3
   =========== =========== ===========
   Row 1       Row 1       Row 1
   Row 2       Row 2       Row 2
   Row 3       Row 3       Row 3
   =========== =========== ===========

.. rst-class:: centered

.. table:: Centered Table

   =========== =========== ===========
   Header1     Header2     Header3
   =========== =========== ===========
   Row 1       Row 1       Row 1
   Row 2       Row 2       Row 2
   Row 3       Row 3       Row 3
   =========== =========== ===========

.. rst-class:: fullwidth

.. table:: Full Width Table

   =========== =========== ===========
   Header1     Header2     Header3
   =========== =========== ===========
   Row 1       Row 1       Row 1
   Row 2       Row 2       Row 2
   Row 3       Row 3       Row 3
   =========== =========== ===========


Using the P-SphinxTheme Table Styling Extension
-----------------------------------------------

:doc:`P-SphinxTheme Table Styling Extension <api/PSphinxTheme.ext.table_styling>`


.. table:: Example
   :widths: 1 2 3
   :header-columns: 1
   :column-alignment: left center right
   :column-dividers: none single double single
   :column-wrapping: nnn

   =========== =========== ===========
   Width x1    Width x2    Width x3
   =========== =========== ===========
   Header 1    Center 1    Right 1
   Header 2    Center 2    Right 2
   Header 3    Center 3    Right 3
   =========== =========== ===========


The same  Table without the special directives

   =========== =========== ===========
   Width x1    Width x2    Width x3
   =========== =========== ===========
   Header 1    Center 1    Right 1
   Header 2    Center 2    Right 2
   Header 3    Center 3    Right 3
   =========== =========== ===========


.. rst-class:: html-toggle

.. _toggle-test-link:

.. index:: Sections; toggleable section examples

Toggleable Section
==================
This section is collapsed by default. But if a visitor follows a link to this section or something within it
(such as :ref:`this <toggle-test-link>`), it will automatically be expanded.

.. rst-class:: html-toggle expanded

Toggleable Subsection
---------------------
Subsections can also be marked as toggleable. This one should be expanded by default.


.. rst-class:: emphasize-children

.. index:: Sections; emphasized children section examples

Section With Emphasized Children
================================
Mainly useful for sections with many long subsections, where a second level of visual dividers would be useful.

Child Section
-------------
Should have slightly lighter background, and be indented.

.. rst-class:: html-toggle

Toggleable Subsection
---------------------
Test of emphasized + toggleable styles. Should be collapsed by default.



.. index:: Code; code examples

Code Examples
=============

.. code-block:: python3

  """An example module docstring to show Pygments style."""

  # Some comment.

  import datetime
  from functools import partial

  number = 123
  word = 'foo'


  class ExampleClass(object):
      """ An example class docstring to show Pygments style.
      """

      def __init__(self, arg1, arg2=None, *args, **kwargs):
          self.attr1 = attr1
          self.attr2 = attr2 or datetime.datetime.now()
          for arg in args:
              print('Argument: '.format(arg))
          for k, v in kwargs.iteritems():
              print('Keyword argument named {}: {}'.format(k, v))

      def call_method(self, arg):
          """ An example method docstring.
          """
          if not isinstance(arg, int):
              raise ValueError('Only ints allowed.')
          self.attr1 = arg

      @property
      def example_property(self):
          """ An example property docstring.
          """
          return self.attr1 * 2


  def example_function(arg1, arg2=None, *args, **kwargs):
      """ An example function docstring to show Pygments style.
      """
      raise NotImplementedError()



Example normal code-block:

.. code-block:: python3

   def my_function():
      "just a test"
      print 8/2


.. python-example:: show/hide prompt

   show/hide the >>> and ... prompts and the output and thus make the code copyable.

   .. code-block:: python3

      >>> alist = [0, 1, 2, 3, 4, 5]
      >>> for x_ in alist:
      ...     print(x_)
      ...
      0
      1
      2
      3
      4
      5
      >>>


.. index:: Examples; autodoc examples

Autodoc
-------

.. automodule:: autodoc_example
   :members:
