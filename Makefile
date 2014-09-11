#!/bin/bash

PYTHON=/usr/bin/env python3

PACKAGE = PSphinxTheme

.PHONY: help clean_docs clean cleanall docs build_force install install_develop uninstall_develop dist pypi_all check_setup init_versioneer code_analysis_pylint

help:
	@echo 'Please use: `make <target>` where <target> is one of'
	@echo '  clean_docs              removes only: `build/sphinx`'
	@echo '  clean                   clean: FILES:`.coverage, MANIFEST, *.pyc, *.pyo, *.pyd, *.o, *.orig` and DIRS: `*.__pycache__`'
	@echo '  cleanall                clean PLUS remove: DIRS: `build, dist, cover, *._pyxbld, *.egg-info` and FILES in MAIN_PACKAGE_PATH: `*.so, *.c` and cython annotate html'
	@echo '  docs                    build the docs for the project'
	@echo '  build_force             build the project: force re-generation of all cython .c files and compile all extension'
	@echo '  install                 force re-compile and install the package'
	@echo '  install_develop         install the package in:development-mode'
	@echo '  uninstall_develop       uninstall the package: development-mode'
	@echo '  dist                    force re-compile and build a source distribution tar file'
	@echo '  pypi_all                force re-compile and re-register/upload (inclusive docs) to pypi'
	@echo '  check_setup             checks the setup.py file'
	@echo '  init_versioneer         inti versioneer for the project'
	@echo '  code_analysis_pylint    pylint the project: ends always with an makefile error?'

clean_docs:
	${PYTHON} setup.py clean --onlydocs
	@echo -e '\n=== finished clean_docs'

clean:
	${PYTHON} setup.py clean
	@echo -e '\n=== finished clean'

cleanall:
	${PYTHON} setup.py clean --all
	@echo -e '\n=== finished cleanall'

docs:
	${PYTHON} setup.py clean --onlydocs
	${PYTHON} setup.py build_sphinx -E
	${PYTHON} setup.py clean
	@echo -e '\n=== finished docs'

build_force:
	${PYTHON} setup.py clean --all
	${PYTHON} setup.py build --force 
	${PYTHON} setup.py clean
	@echo -e '\n=== finished build_force'

install:
	${PYTHON} setup.py clean --all
	${PYTHON} setup.py build --force 
	${PYTHON} setup.py install 
	${PYTHON} setup.py clean
	@echo -e '\n=== finished install'

install_develop:
	${PYTHON} setup.py clean --all
	${PYTHON} setup.py develop --exclude-scripts
	${PYTHON} setup.py clean
	@echo -e '\n=== finished install_develop'

uninstall_develop:
	${PYTHON} setup.py develop --uninstall
	${PYTHON} setup.py clean
	@echo -e '\n=== finished uninstall_develop'

dist:
	${PYTHON} setup.py clean --all
	${PYTHON} setup.py sdist 
	${PYTHON} setup.py clean
	@echo -e '\n=== finished dist'

pypi_all:
	${PYTHON} setup.py clean --all
	${PYTHON} setup.py check
	${PYTHON} setup.py register
	${PYTHON} setup.py sdist upload
	${PYTHON} setup.py build_sphinx upload_docs
	${PYTHON} setup.py clean
	@echo -e '\n=== finished pypi_all'

check_setup:
	${PYTHON} setup.py clean
	${PYTHON} setup.py check
	${PYTHON} setup.py clean
	@echo -e '\n=== finished check_setup'

init_versioneer:
	${PYTHON} setup.py versioneer
	@echo -e '\n=== finished init_versioneer'

code_analysis_pylint:
	pylint -f colorized PSphinxTheme
	@echo -e '\n=== finished code_analysis_pylint'
