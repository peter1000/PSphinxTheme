# taken from: https://github.com/espdev/sphinx-fancy-theme/blob/master/docs/source/example.py

"""An example module to show autodoc style.

Contains an example constant, :class:`Storage` class for storing objects and helper function :func:`store_integers` for
storing only integers.


"""
from datetime import datetime


#: Example integer constant.
INT_CONSTANT = 1

#: Example integer constant.
STR_CONSTANT = 'string'


class Storage(object):
   """A class for storing objects.

   This is an example class to show autodoc style.

   It stores a list of objects and saves date of last appended item.

   .. python-example::

      .. code-block:: python3
      
         >>> storage = Storage(['foo', 'bar'])
         >>> storage.items
         ['foo', 'bar']
         >>> storage.last_updated
         datetime.datetime(2013, 8, 15, 13, 41, 38, 515797)
         >>> storage.add_item('baz')
         >>> storage.items
         ['foo', 'bar', 'baz']
         >>> storage.last_updated
         datetime.datetime(2013, 8, 15, 13, 41, 40, 595544)

   .. table:: example of table with autodoc and dividers
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
      
   :param items:
      Optional list of items to start with.
   """
   def __init__(self, items=None):
      #: List of items, add new item using :meth:`add_item`.
      self.items = items or []
      #: :py:class:`datetime.datetime` of last item update, will be set
      #: to :py:meth:`datetime.datetime.now` on object instantiation.
      self.last_updated = datetime.now()

   def add_item(self, item):
      """ Append item to the list.

      :attr:`last_updated` will be set to :py:meth:`datetime.datetime.now`.

      :param item:
         Something to append to :attr:`items`.

      """
      self.items.append(item)
      self.last_updated = datetime.now()


def store_integers(items, allow_zero=True):
   """ Store integers from the given list in a storage.

   This is an example function to show autodoc style.

   Return :class:`Storage` instance with integers from the given list.

   .. python-example::

      .. code-block:: python3
         
         >>> storage = store_integers([1, 'foo', 2, 'bar', 0])
         >>> storage.items
         [1, 2, 0]
         >>> storage = store_integers([1, 'foo', 2, 'bar', 0], allow_zero=False)
         >>> storage.items
         [1, 2]

   :param items:
      List of objects of any type, only :class:`int` instances will be stored.
   :param allow_zero:
      Boolean -- if ``False``, ``0`` integers will be skipped.
      Defaults to ``True``.

   :return:
      class: storage
      
      .. table:: example of table with autodoc and dividers nested in `table field-list`
         :widths: 3 2 1
         :column-alignment: left center right
         :column-wrapping: true true false
         :column-dividers: single single double single


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
   """
   ints = [x for x in items if isinstance(x, int) and (allow_zero or x != 0)]
   storage = Storage(ints)
   return storage
