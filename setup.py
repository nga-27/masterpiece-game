#!/usr/bin/env python
# Based on: https://github.com/kennethreitz/setup.py/blob/master/setup.py
"""
Setup tools
Use setuptools to install package dependencies. Instead of a requirements file you
can install directly from this file.
`pip install .`
You can install dev dependencies by targetting the appropriate key in extras_require
```
pip install .[dev] # install requires and test requires
pip install '.[dev]' # install for MAC OS / zsh

```
See: https://packaging.python.org/tutorials/installing-packages/#installing-setuptools-extras
"""
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'masterpiece-game'
DESCRIPTION = 'Emulate the old 60s-70s game of buying/selling art.'
URL = 'https://github.mmm.com/nga-27/masterpiece-game'
EMAIL = 'namell91@gmail.com'
AUTHOR = 'Nick Amell'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.0.2'

# What packages are required for this module to be executed?
REQUIRES = [
    "fastapi==0.63.0",
    "uvicorn==0.13.4",
    "requests==2.25",
    "pillow==8.1.2"
]

REQUIRES_DEV = [
    'colorama==0.4.3',
    'pylint==2.7.4',
    'pycodestyle==2.6.0',
    'pytest==6.2.3',
    'pytest-env==0.6.2',
    'pytest-cov==2.11.1',
    'pylint-fail-under==0.3.0',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*"
            "tests.*",
            "tests"
        ]
    ),
    install_requires=REQUIRES,
    extras_require={
        'dev': REQUIRES_DEV,
    },
    include_package_data=True,
    license='UNLICENSED',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
