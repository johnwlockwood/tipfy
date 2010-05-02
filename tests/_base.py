# -*- coding: utf-8 -*-
"""
To run the tests, first install the following packages:

    easy_install nose
    easy_install nosegae==0.1.7
    easy_install webtest
    easy_install gaetestbed
    easy_install coverage

Then run the tests from the repository root:

    nosetests -d --with-gae --without-sandbox --cover-erase --with-coverage --cover-package=tipfy --gae-application=./buildout/app
"""
import os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PATHS = [BASE, os.path.join(BASE, 'buildout', 'app'),]

for path in PATHS:
    if path not in sys.path:
        sys.path.insert(0, path)
