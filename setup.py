#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Copyright 2014 Michael Helmling
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation

import os
import fnmatch
import io
import re
from os.path import join, dirname, abspath

from setuptools import setup
from Cython.Build import cythonize
import numpy as np


here = abspath(dirname(__file__))


def makeExtensions():
    """Returns an Extension object for the given submodule of lpdecoding."""

    sources = []
    for root, dirnames, filenames in os.walk(join(here, 'lpdec')):
        for filename in fnmatch.filter(filenames, '*.pyx'):
            sources.append(join(root, filename))
    extensions = cythonize(sources, include_path=[np.get_include()])
    return extensions


with io.open(os.path.join(here, 'lpdec', '__init__.py'), 'r', encoding='UTF-8') as f:
    version_file = f.read()
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', version_file, re.M)
    version = version_match.group(1)

setup(
    name='lpdec',
    version=version,
    author='Michael Helmling',
    author_email='helmling@uni-koblenz.de',
    install_requires=['numpy', 'sqlalchemy', 'cython'],
    ext_modules=makeExtensions(),
    packages=['lpdec'],
    test_suite='test',
)