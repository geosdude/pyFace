#!/bin/bash
#from distutils.core import setup
from setuptools import setup

setup(
    name='BaseTools',
    version='0.1.1',
    author='Richard R. Polk, Jr.',
    author_email='geos.dude@gmail.com',
    packages=['base_Tools'] #, 'base_Tools.test'],
    #scripts=['bin/stowe-towels.py', 'bin/wash-towels.py'],
    license='LICENSE.txt',
    description='Useful python-related stuff.',
    #long_description=open('README.txt').read(),
)
