"""
setup / install / distribute
"""


# ===========================================================================================================================
# init script env -- ensure cwd = root of source dir
# ===========================================================================================================================
from inspect import (
   getfile,
   currentframe
)
from shutil import rmtree
from os import (
   remove as os_remove,
   walk as os_walk,
)
from os.path import (
   abspath,
   dirname,
   exists as path_exists,
   isfile,
   join as path_join,
   splitext as path_splitext,
)
from sys import (
   argv as sys_argv,
   exit as sys_exit,
   platform as sys_platform,
   version_info as sys_version_info,
)

from setuptools import (
   Command,
   find_packages,
   setup,
)

import versioneer


versioneer.VCS = 'git'
versioneer.versionfile_source = 'PSphinxTheme/_version.py'
versioneer.versionfile_build = 'PSphinxTheme/_version.py'
versioneer.tag_prefix = ''  # tags are like 1.1.0
versioneer.parentdir_prefix = 'PSphinxTheme-'  # dirname like 'PSphinxTheme-1.1.0'

_version = versioneer.get_version()

SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PACKAGE_NAME = 'PSphinxTheme'
ROOT_PACKAGE_PATH = path_join(dirname(SCRIPT_PATH), PACKAGE_NAME)
MAIN_PACKAGE_PATH = path_join(ROOT_PACKAGE_PATH, PACKAGE_NAME)

from PSphinxTheme import TESTED_HOST_OS

if sys_version_info[:2] < (3, 4) or sys_platform == 'win32':
   print('''
\nPSphinxTheme is only tested with Python 3.4.1 or higher:\n  current python version: {0:d}.{1:d}\n\n

TESTED_HOST_OS: {3:}
'''.format(sys_version_info[:2][0], sys_version_info[:2][1], TESTED_HOST_OS))

# check some untested options
for option_temp in {'bdist_dumb', 'bdist_rpm', 'bdist_wininst', 'bdist_egg'}:
   if option_temp in sys_argv:
      print('''

TESTED_HOST_OS you specified an untested option: <{}>\n\n

   This might work or might not work correctly

'''.format(option_temp))


# ===========================================================================================================================
# helper classes, functions
# ===========================================================================================================================
def read_requires(filename):
   """ Helper: read_requires
   """
   requires = []
   with open(filename, 'r') as file_:
      for line in file_:
         line = line.strip()
         if not line or line.startswith('#'):
            continue
         requires.append(line)
   return requires


class CleanCommand(Command):
   """ Custom distutils command to clean
   """
   description = '''Custom clean: FILES:`.coverage, MANIFEST, *.pyc, *.pyo, *.pyd, *.o, *.orig`
                    and DIRS: `*.__pycache__`'''
   user_options = [
      ('all', None,
         '''remove also: DIRS: `build, dist, cover, *._pyxbld, *.egg-info` and
            FILES in MAIN_PACKAGE_PATH: `*.so, *.c` and cython annotate html'''
      ),
      ('onlydocs', None,
         'remove ONLY: `build/sphinx`'
      ),
   ]

   # noinspection PyAttributeOutsideInit
   def initialize_options(self):
      self.all = False
      self.onlydocs = False
      self.onlyhtml = False

   def finalize_options(self):
      pass

   def run(self):
      need_normal_clean = True
      exclude_files = []
      remove_files = []
      remove_dirs = []

      # remove ONLY: `build/sphinx`
      if self.onlydocs:
         need_normal_clean = False
         dir_path = path_join(ROOT_PACKAGE_PATH, 'build', 'sphinx')
         if path_exists(dir_path):
            remove_dirs.append(dir_path)

      # remove also: DIRS: `build, dist, cover, *.egg-info, *._pyxbld`
      # and FILES in MAIN_PACKAGE_PATH: `*.so, *.c` and cython annotate html
      if self.all:
         need_normal_clean = True
         for dir_ in {'build', 'dist', 'cover'}:
            dir_path = path_join(ROOT_PACKAGE_PATH, dir_)
            if path_exists(dir_path):
               remove_dirs.append(dir_path)
         for root, dirs, files in os_walk(ROOT_PACKAGE_PATH):
            for dir_ in dirs:
               if '_pyxbld' in dir_ or 'egg-info' in dir_:
                  remove_dirs.append(path_join(root, dir_))

         # remove FILES in MAIN_PACKAGE_PATH: `*.so, *.c` and cython annotate html
         for root, dirs, files in os_walk(MAIN_PACKAGE_PATH):
            for file_ in files:
               if file_ not in exclude_files:
                  if path_splitext(file_)[-1] in {'.so', '.c'}:
                     remove_files.append(path_join(root, file_))

                  tmp_name, tmp_ext = path_splitext(file_)
                  if tmp_ext == '.pyx':
                     # Check if we have a html with the same name
                     check_html_path = path_join(root, tmp_name + '.html')
                     if isfile(check_html_path):
                        remove_files.append(check_html_path)

      # do the general clean
      if need_normal_clean:
         for file_ in {'.coverage', 'MANIFEST'}:
            if path_exists(file_):
               remove_files.append(file_)

         for root, dirs, files in os_walk(ROOT_PACKAGE_PATH):
            for file_ in files:
               if file_ not in exclude_files:
                  if path_splitext(file_)[-1] in {'.pyc', '.pyo', '.pyd', '.o', '.orig'}:
                     remove_files.append(path_join(root, file_))
            for dir_ in dirs:
               if '__pycache__' in dir_:
                  remove_dirs.append(path_join(root, dir_))

      # REMOVE ALL SELECTED
      # noinspection PyBroadException
      try:
         for file_ in remove_files:
            if path_exists(file_):
               os_remove(file_)
         for dir_ in remove_dirs:
            if path_exists(dir_):
               rmtree(dir_)
      except Exception:
         pass


def check_release():
   """ Check that only full git version (x.x or x.x.x) are used for 'register,
   """
   # noinspection PySetFunctionToLiteral
   options_to_check = set({'register', 'upload', 'upload_docs'})
   for option_ in options_to_check:
      if option_ in sys_argv:

         # Check
         if '-' in _version:
            sys_exit('''

               === Error ===    check_release(): option_: <{}> in options_to_check: <{}>

               For a release: only full git version (x.x or x.x.x) are supported:
                  You must commit any changes before and TAG the release.
                     _version: <{}>.

               '''.format(option_, options_to_check, _version)
            )


check_release()

cmdclass = versioneer.get_cmdclass()
cmdclass.update({
   'clean': CleanCommand,
})


# ===========================================================================================================================
# setup
# ===========================================================================================================================
setup(
   name='PSphinxTheme',
   version=_version,
   author='peter1000',
   author_email='https://github.com/peter1000',
   url='https://github.com/peter1000/PSphinxTheme',
   license='BSD-3-Clause',
   packages=find_packages(),
   include_package_data=True,
   install_requires=read_requires('requirements.txt'),
   use_2to3=False,
   zip_safe=False,
   platforms=['Linux'],
   cmdclass=cmdclass,
   description="A sphinx theme I use for most projects. Derivative of Eli Collins's cloud_sptheme.",
   long_description=open('README.rst', 'r').read(),
   classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python :: 3',
      'Topic :: Documentation',
      'Topic :: Software Development :: Documentation',
   ],
   keywords='python sphinx theme doc extension',
)
