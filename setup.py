#!/usr/bin/env python3

VERSION = '1.0.0'
DESCRIPTION = 'DagKnows Automation Framework'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='dagknows',
    version=VERSION,
    description=DESCRIPTION,
    license=None,
    long_description="Test Automation Framework for Lendica",
    url='https://github.com/',
    author="Pranav Sharma",
    author_email='pranav165@gmail.com',
    install_requires=[
        'pytest',
        'retry',
        'pytest-html',
        'flake8',
        'selenium',
        'webdriver-manager',
    ],
    provides=[],
    packages=find_packages(),
    scripts=[]
)
