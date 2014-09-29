===============
Release History
===============


.. _whats-new:

Version 1.3.4     2014-09-29
============================

Fixes/Other Changes:
--------------------

   - updated: Projects using PSphinxTheme


Version 1.3.3     2014-09-13
============================

Features:
---------

   - added css styling option for docstrings classes: descclassname / descname

      - ``docstring_descclassname_color``
      - ``docstring_descclassname_font_weight``
      - ``docstring_descclassname_font_size``

      - ``docstring_descname_color``
      - ``docstring_descname_font_weight``
      - ``docstring_descname_font_size``


Fixes/Other Changes:
--------------------

   - FIXES: :issue:`2`.

      - `requirement.txt`: adjusted Sphinx to exact version 1.2.3

   - replaced: `basic.css_t` with an version based on Sphinx-1.2.3
   - adjusted all theme


Version 1.3.2     2014-09-12
============================

Features:
---------

Fixes/Other Changes:
--------------------

   - fixed to long line in docs
   - changed the background color for: example-admonitions
   - removed info on using the theme with: ReadTheDocs
   - adjusted: README.rst


Version 1.3.1     2014-09-11
============================

Features:
---------

   - added check for Example Admonitions code-block highlighter

      - changed also all `.. code-block:: python` to `.. code-block:: python3`

   - docs: added longer LCONF example


Fixes/Other Changes:
--------------------

   - updated requirements: added LconfPygmentsLexer
   - small `Makefile` adjustments
   - small `setup.py` adjustments


Version 1.3.0     2014-09-10
============================


Features:
---------

   - added new admonitions:

      - ``.. json-example::``
      - ``.. lconf-example::``

Fixes/Other Changes:
--------------------

   - `table_styling.py`: removed function `_split_argument_list`
   - added to some css files: ``highlight-python3`` - `python3` pygments syntax highlighter
   - fixed doc for option: `code_boarder_color` info inf *main_cloud_theme.rst*
   - updated/added docs:

      - install.rst


Version 1.2.5     2014-09-08
============================

Features:
---------

   - added new sub-theme: `p-greycreme`

Fixes/Other Changes:
--------------------

   - updated doc: theme_test.rst to reference the real issue: 1
   - added some info about the sticky sidebar


Version 1.2.4     2014-09-02
============================

Fixes/Other Changes:
--------------------

   - added info about warnings at installation


Version 1.2.3     2014-09-02
============================

Fixes/Other Changes:
--------------------

   - improved sdist: excluding *__pycache__* folders
   - archived files in ``themes_dev_resources`` and moved them to: ``External_Sources``


Version 1.2.2     2014-08-24
============================

Features:
---------
   - allow proper ``table_styling`` in docstrings table-lists: e.g. return statements.

   - use our own base.css instead of the one from sphinx. copy of base.css: taken from Sphinx (1.3a0dev-20140821)

      - removed all ``!important`` from basic.css_t


Fixes/Other Changes:
--------------------

   - removed from extension: ``table_styling``

      - table_styling_embed_css: EMBED_KEY
      - table_styling_class: CLASS_KEY
      - function: prepare_builder()

   - removed: ``PSphinxTheme/ext/table_styling.css``

   - removed all ``!important`` from cloud.css_t


Version 1.1.2     2014-08-22
============================

Features:
---------

   .. warning:: ``PSphinxTheme/ext/perpage.py``

      - renamed: ``perpage.py`` to ``sidebarlogo_perpag.py``

      - renamed: ``perpage_html_logo`` to ``sidebarlogo_perpage_dict``

         .. important::

            dict uses now as key the ``image_name`` or ``None`` and the value is a ``set`` of pages: see the extension docs

   - added a project: Makefile


Fixes/Other Changes:
--------------------

   - some documentation improvements

      - added documentation: Projects using PSphinxTheme

   - changed: utils.Err(): parameter info from string to a list

   - changed options default: ``sidebar_prev_next=false``

   - update: setup.py CleanCommand()

   - updated Pycharm dict

   - FIXED: pylint error:

      - E:132,14: Instance of 'PSphinxAdmonition' has no 'node_class' member (no-member)
      - E:134,15: Instance of 'PSphinxAdmonition' has no 'label' member (no-member)


Version 1.0.0     2014-08-18
============================

Features:
---------

   - Added `copybutton.js` to `static/cloud.js_t`
      Adds a [>>>] button on the top-right corner of code samples to hide
      the >>> and ... prompts and the output and thus make the code copyable.
   - Added local fonts:
      `static/local_fonts.css` and `static/fonts`
   - Added function: Utils.set_psphinxtheme
      Returns common sphinx settings for *P-SphinxTheme* to be uses in ``conf.py``
   - Added *theme option*:

      - ``sidebar_prev_next`` to include or disable them
      - ``header_textshadowcolor``
      - ``quotedtxtfont``

   - Added sphinx extension:

      - ``ext/psphinx_admonitions.py``
         this adds all official P-SphinxTheme admonitions
      - ``ext/relbar_links.py``
         this is based on the previous ``relbar_toc`` but is more flexible  adding any number of entries

      .. note::

         - for sphinx directive ``deprecated``: there is also support in theme option
         - for the extension: ``sphinx.ext.todo``: there is also support in theme option

   - changed icons

   - Added / rewrote much of the available options.

Fixes/Other Changes:
--------------------

   - Changed defaults

      - ``bodyfont`` to: 'Noto Sans'
      - ``headfont`` to 'Noto Serif'
      - ``max_width`` to 14in
      - ``sidebarwidth`` to int: '230'

   - Reformatted code

      - to 3 spaces indent
      - max 125 char lines

   - Renamed code

      - main package: to CapWords: PSphinxTheme
      - other parts too: especial the themes as they might not work with the original `cloud_sptheme`

      - *theme option*
         ``footerbgcolor`` to ``main_boarder_bg_color``
         ``sidebartrimcolor`` to ``sidebar_boarder_color``
         ``table_trim_color`` to ``table_boarder_color``
         ``codetrimcolor`` to ``code_boarder_color``
         ``bodyrimcolor`` to ``body_boarder_color``
         ``quotetrimcolor`` to ``quoted_boarder_color``
         ``sectiontrimcolor`` to ``section_boarder_color``
         ``admonition_trim_color`` to ``admonition_boarder_color``
         ``highlighttoc`` to ``sidebar_highlighttoc``
         ``popuptoc`` to ``sidebar_popuptoc``
         ``quotebgcolor`` to ``quotedbgcolor``

   - Removed

      - *theme option*
         ``sidebar_master_title``

      - make_helper.py
      - PY2 related checks as PY3 is expected
      - legacy aliases
      - logging

      - extension:

         - autodoc_sections.py
         - relbar_links.py

   - Updated jquery.cookie.js to version: v1.4.1

   - Fixed

      - table_styling.py class_option_list() had an error: Unresolved reference for `directive`

   - number of undocumented changes / additions

Project start 2014-08-06
========================

   - project start
      `PSphinxTheme` alas *P-SphinxTheme* is based on **cloud_sptheme** version 1.6 checked out on 20140806:
      `<https://bitbucket.org/ecollins/cloud_sptheme>`_ Thanks goes to: **Eli Collins**
