#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0, 'InfoR')

sys.path.pop(0)

packages = ['InfoR',
			'InfoR.Examples']

setup(
	name='infor',
	version='0.20',
	author='Janu Verma',
	author_email='jv367@cornell.edu',
	description='A Python package for Information Retrieval',
	#url='https://github.com/Jverma/InfoR',
	platforms=['Linux','Mac OSX', 'Windows', 'Unix'],
	classifiers=[
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
	'License :: MIT License',
	'Operating System :: OS Independent',
	'Progamming Language :: Python',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Topic :: Scientific/Engineering :: Information Retrieval',
	'Topic :: Scientific/Engineering :: Machine Learning',
	'Topic :: Scientific/Engineering :: Natural Language Processing'],
	packages=packages,
	package_data={'InfoR':['Data/*.txt']},
	license='MIT'
	)			
	