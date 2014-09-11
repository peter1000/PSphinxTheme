

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


ReadTheDocs
===========
To use this theme on `<http://readthedocs.org>`_:

1. If it doesn't already exist, add a pip ``requirments.txt`` file to your project.
   It should contain a minimum of the following lines::

      Sphinx>=1.2
      PSphinxTheme>=1.3.1

   ... as well as any other build requirements for your project's documentation.

2. When setting up your project on ReadTheDocs go to: *Import an existing project*

   - *Name* field: e.g. ``PSphinxTheme``
   - *Repo* field: e.g. ``https://github.com/peter1000/PSphinxTheme.git``
   - *Repository type* field: e.g. ``Git``
   - *Description* field: e.g. ``A sphinx theme I use for most projects. Derivative of "Eli Collins's cloud_sptheme".``
   - *Language* field: e.g. ``English``
   - *Documentation type* field: e.g. ``Sphinx Html``
   - *Project URL* field: e.g use the one from github / bitbucket etc.: ``https://github.com/peter1000/PSphinxTheme``
   - *Canonical URL* field: e.g. use the one from readthedocs: ``http://psphinxtheme.readthedocs.org/``
   - *Tags* field: e.g. use the one from setup.py keywords *but* comma-separated: ``python, sphinx, theme, doc, extension``

3. Go to Admin > Advanced Settings.

   - *Use virtualenv* field: Install your project inside a virtualenv using setup.py install: ``Tick it``
   - *Requirements file* field: e.g. requirements.txt
   - *Single version* field: A single version site has no translations and only your "latest" version: ``Tick it``
   - *Python configuration file* field: e.g. ``docs/conf.py``
   - *Default branch* field: e.g. ```leave it empty``
   - *Default version* field: e.g. ``latest``
   - *Privacy Level* field: e.g. ``Public``
   - *Use system packages* field: e.g. ``leave it unticked``
   - *Python interpreter* field: e.g. ``CPython 3.x``
   - *Analytics code* field: e.g. ``leave it empty``
   - *Number of Major versions* field: e.g. ``2``
   - *Number of Minor versions* field: e.g. ``2``
   - *Number of Point versions* field: e.g. ``2``


4. ReadTheDocs will now automatically download the latest version of :mod:`!PSphinxTheme` when building your documentation.


Documentation
=============
The latest copy of this documentation should always be available at: `<http://packages.python.org/PSphinxTheme>`_

If you wish to generate your own copy of the documentation, you will need to:

#. Download the :mod:`!PSphinxTheme` source.
#. If not already installed - install `Sphinx <http://sphinx-doc.org/>`_
#. If not already installed - install `LconfPygmentsLexer <https://github.com/peter1000/LconfPygmentsLexer>`_
#. From the `PSphinxTheme` source directory, run ``python3 setup.py build_sphinx -E``.
#. Once Sphinx is finished, point a web browser to the file :samp:`{SOURCE}/build/sphinx/html/index.html`.
