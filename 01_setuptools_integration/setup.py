#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

py_ver = "%s%s" % (sys.version_info.major, sys.version_info.minor)

setup(
    name="hello",
    version="0.1",
    py_modules=["hello"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        hello{py_ver}=hello:cli
    """.format(py_ver=py_ver),
)