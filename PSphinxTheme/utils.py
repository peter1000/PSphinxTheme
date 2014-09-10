"""
=====================================
PSphinxTheme.utils - helper functions
=====================================

Overview
========
This module defines a couple of helper functions.

Functions
=========
.. autofunction:: set_psphinxtheme

.. autofunction:: get_psphinxtheme_root_dir

.. autofunction:: is_cloud_theme

"""
from inspect import (
   getfile,
   currentframe
)
from os import listdir
from os.path import (
   abspath,
   dirname,
   isfile,
   join as path_join,
)

from PSphinxTheme import TESTED_HOST_OS


class Err(Exception):
   """ Prints an own raised ProjectError

   :param error_type: (str) to specify mostly from which part the error comes: e.g. CONFIG
   :param info: (list) list of strings (text info) to print as message: each list item starts at a new line
   """

   def __init__(self, error_type, info):
      Exception.__init__(self, error_type, info)
      self.__error_type = error_type
      self.__info = '\n'.join(info)
      self.__txt = '''

========================================================================
PSphinxTheme-{} ERROR:


  {}

This `PSphinxTheme` was tested with:
  HOST OS: {}
========================================================================

'''.format(self.__error_type, self.__info, TESTED_HOST_OS)
      print(self.__txt)


# ===========================================================================================================================
# public helpers
# ===========================================================================================================================
# noinspection PyUnusedLocal
def set_psphinxtheme(name):
   """ Returns *P-SphinxTheme* related basic settings and checks also if ``name`` is a valid `PSphinxTheme` name.

  This is designed to be used within Sphinx's ``conf.py`` file.

   .. seealso:: The :ref:`P-SphinxTheme Usage Example <usage_example>`.

   :param name: (str) a valid *P-SphinxTheme* theme name
   :return: (tuple) [html_theme_path], html_theme, needs_sphinx
   """
   needs_sphinx = '1.2'
   html_theme_path = path_join(get_psphinxtheme_root_dir(), 'themes')
   html_theme = ''
   if not isfile(path_join(html_theme_path, name, 'theme.conf')):
      raise Err('Utils.set_psphinxtheme()', [
            'name: <{}> seems not to be a valid `PSphinxTheme`: <{}>'.format(name, listdir(html_theme_path))
         ]
      )
   else:
      html_theme = name
   return [html_theme_path], html_theme, needs_sphinx


def get_psphinxtheme_root_dir():
   """ :return: (str) path of the *P-SphinxTheme* root dir
   """
   return dirname(abspath(getfile(currentframe())))


def is_cloud_theme(name):
   """ :return: (bool) True if name is a valid *P-SphinxTheme* theme name.
   """
   html_theme_path = path_join(get_psphinxtheme_root_dir(), 'Themes')
   return isfile(path_join(html_theme_path, name, 'theme.conf'))
