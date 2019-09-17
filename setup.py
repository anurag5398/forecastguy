# -*- coding: utf-8 -*-
from setuptools import setup

setup(
      name = 'forecastguy',
      url = 'notyet',
      author = 'Anurag Srivastava',
      author_email = 'anurags2898@gmail.com',
      packages = ['forecastguy'],
      install_requires = ['requests','urllib3'],
      version = '0.1',
      license = 'GNU General Public License v3.0',
      description = 'CLI for finding forecast',
      long_description = open('README.txt').read(),
      scripts = ['forecastguy/forecast.py']
      )