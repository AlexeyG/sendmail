#!/usr/bin/env python

from setuptools import setup

setup(name = 'sendmail',
      version = '1.0',
      description = 'Python Distribution Utilities',
      author = 'Alexey Gritsenko',
      author_email = 'grizenko.a@gmail.com',
      packages = ['sendmail'],
      install_requires = ['lepl']
     )
