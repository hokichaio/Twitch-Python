#!/usr/bin/env python

import os

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    readme = f.read()

pipfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pipfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pipfile['dev-packages'], r=False)
setup_requirements = ['pipenv', 'setuptools']

setup(
    author='Petter Kraabøl',
    author_email='petter.zarlach@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description='Twitch module for Python',
    install_requires=requirements,
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='Twitch API',
    name='twitch-python',
    packages=find_packages(),
    python_requires=">=3.7",
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/PetterKraabol/Twitch-Python',
    version='0.0.13',
    zip_safe=True,
)
