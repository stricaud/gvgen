#!/usr/bin/python
import setuptools
from distutils.core import setup

setup(name="GvGen",
            version="1.0",
            author="Sebastien Tricaud",
            author_email="sebastien@honeynet.org",
            description="Generate clear Graphviz Graphs which can be edited manually later on.",
            url="http://www.github.com/stricaud/gvgen/",
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            py_modules=["gvgen"])
