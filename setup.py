#!/usr/bin/env python

from distutils.core import setup

setup(name='AutoBlazon',
      version='0.1',
      description='Parse and Blazon Heraldic Crests',
      author='Lady Red / Chris Beacham',
      author_email='mcscope@gmail.com',
      url='https://github.com/mcscope/autoblazon',
      packages=['autoblazon'],
      install_requires=["lark-parser"],
     )
