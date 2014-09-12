

=========================
Installation Instructions
=========================

.. index:: P-Sphinx Theme; requirements

Requirements
============
- Python 3

   - for python2 look at the original `cloud_sptheme <https://bitbucket.org/ecollins/cloud_sptheme>`_ by **Eli Collins**

- `Sphinx <http://sphinx-doc.org/>`_
- `LconfPygmentsLexer <https://github.com/peter1000/LconfPygmentsLexer>`_


.. index:: P-Sphinx Theme; installation

Installing
==========

.. shell-example::

   To install from pypi using ``pip/pip3``

   .. code-block:: sh

      $ pip3 install PSphinxTheme

   To install from source using ``setup.py``

   .. code-block:: sh

      $ python3 setup.py build
      $ sudo python3 setup.py install


.. important:: Warnings at installation

   .. code-block:: sh

      $ warning: no previously-included files matching '__pycache__' found under directory '*'

   This can be ignored `__pycache__` is excluded in the `MANIFEST.in` file


.. index:: readthedocs.org; installation on

Documentation
=============
The latest copy of this documentation should always be available at: `<http://packages.python.org/PSphinxTheme>`_

If you wish to generate your own copy of the documentation, you will need to:

#. Download the :mod:`!PSphinxTheme` source.
#. If not already installed - install `Sphinx <http://sphinx-doc.org/>`_
#. If not already installed - install `LconfPygmentsLexer <https://github.com/peter1000/LconfPygmentsLexer>`_
#. From the `PSphinxTheme` source directory, run ``python3 setup.py build_sphinx -E``.
#. Once Sphinx is finished, point a web browser to the file :samp:`{SOURCE}/build/sphinx/html/index.html`.
