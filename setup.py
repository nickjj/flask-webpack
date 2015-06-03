#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    print 'Flask-Webpack needs setuptools in order to build. ' + \
          'Install it using your package manager ' + \
          '(usually python-setuptools) or via pip (pip install setuptools).'
    sys.exit(1)

setup(name='Flask-Webpack',
      version=open('VERSION', 'r').read()[:-1],
      author='Nick Janetakis',
      author_email='nick.janetakis@gmail.com',
      url='https://github.com/nickjj/flask-webpack',
      description='Flask extension for managing assets with Webpack.',
      license='GPLv3',
      install_requires=['setuptools', 'Flask'],
      tests_require=['pytest'],
      packages=['flask_webpack'],
      package_data={'Flask-Webpack': ['VERSION']},
      zip_safe=False,
      data_files=[])
