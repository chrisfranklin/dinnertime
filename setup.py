#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='dinnertime',
    version='1.0',
    description="",
    author="Chris Franklin",
    author_email='chris@piemonster.me',
    url='',
    packages=find_packages(),
    package_data={'dinnertime': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
