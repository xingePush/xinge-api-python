#!/usr/bin/env python
# -*-coding:utf-8-*-

import ast
import re
try:
    from setuptools import setup
except:
    from distutils.core import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('xinge_push/__init__.py') as f:
    VERSION = ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1))

NAME = "xinge_push"

PACKAGES = ["xinge_push", ]
DESCRIPTION = "xinge Push API for Python(http://xg.qq.com)."
LONG_DESCRIPTION = open("README.rst").read()

KEYWORDS = ["xinge", "Android Push", "iOS Push", "push"]

AUTHOR = "yang"
AUTHOR_EMAIL = "1020211152@qq.com"
LICENSE = "MIT"

URL = "https://github.com/xingePush/xinge-api-python"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms="any",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
