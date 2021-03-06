############################################################################
#   Copyright 2017 Rigetti Computing, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
############################################################################
from setuptools import setup, find_packages
from forestopenfermion import __version__

# Readme file as long_description:
long_description = open('README.rst').read()

setup(
    name='forestopenfermion',
    version=__version__,
    author='Rigetti Computing',
    author_email='softapps@rigetti.com',
    description='A plugin allowing OpenFermion to interface with Forest.',
    long_description=long_description,
    license='Apache 2',
    install_requires=[
        'scipy >= 0.18.0',
        'numpy >= 1.11.0',
        'openfermion == 0.1a0',
        'pyquil >= 1.1.0',
        'future'
    ],
    packages=find_packages(exclude=["tests"])
)
