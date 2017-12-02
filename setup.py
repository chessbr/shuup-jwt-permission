# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="shuup-jwt-permission",
    version="0.1.0",
    description="Add JWT Permission to Shuup REST API",
    license="MIT",
    author="Christian Hess",
    author_email="christianhess.rlz@gmail.com",
    packages=find_packages(),
    install_requires=[
        "rest-jwt-permission>=0.1.1,<2"
    ],
    long_description=long_description,
    url="https://github.com/chessbr/shuup-jwt-permission",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP",
        "Intended Audience :: Developers"
    ]
)
