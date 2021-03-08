# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='demo',
    version='0.1.0',
    description='Avaliação em Python by Silverio Leite Jr - (11)96020 6334 ',
    long_description=readme,
    author='Silverio Leite Jr',
    author_email='silverio.leitejr@og1.com.br',
    url='https://github.com/silverioleitejr/avaliacao-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

