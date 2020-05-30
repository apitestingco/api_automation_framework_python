from setuptools import setup, find_packages

setup(name = 'api-test',
version = '1.0',
description = 'API test',
author = 'Pramod Dutta',
packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)