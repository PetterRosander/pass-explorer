#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='pass-explorer',
            version='-',
            description='N/A',
            maintainer='Petter',
            platforms=['unix'],
            scripts=["bin/pass-explorer"],
            packages=find_packages()
            )
