#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

from setuptools import setup
from setuptools import find_packages

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file, yaml.Loader)

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'wazo_calld.plugins': [
            'wp465 = wazo_calld_mobile_group.plugin:Plugin'
        ],
    },
)
