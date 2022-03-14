# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
	name = 'servier',
	version='beta',
	author='mc',
	author_email='mxxxxx.cxxxxx@gmail.com',
	description='Binary prediction through deep learning model from SMILES molecule representation',
	packages=['servier'], entry_points={'console_scripts':['servier = servier.__init__:predict']}
	)