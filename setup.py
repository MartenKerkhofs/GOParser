from setuptools import setup, find_packages, Command
from codecs import open
import os
from os import path

here = path.abspath(path.dirname(__file__))
description = 'GOparser - A Python Framework for Working with Gene Ontology (GO) Terms and Annotations'
version = '1.1.3'

long_description = ''
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

class CleanCommand(Command):
    """Removes files generated by setuptools.

    """
    # see https://github.com/trigger/trigger/blob/develop/setup.py
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        error_msg = 'You must run this command in the package root!'
        assert os.getcwd() == here, error_msg
        os.system('rm -rf ./dist ./build ./*.egg-info ')

setup(
    name = 'goparser',

    version = version,

    description = description,
    long_description = long_description,

    # homepage
    url = 'https://github.com/flo-compbio/goparser',

    author = 'Florian Wagner',
    author_email = 'florian.wagner@duke.edu',

    license='GPLv3',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords = 'gene ontology biology bioinformatics',

    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages = ['goparser'],

    install_requires = ['genometools'],

    # development dependencies
    extras_require = {
            'docs': ['sphinx','sphinx_rtd_theme']
    },

    # data
    #package_data={
    #},

    # data outside package
    #data_files=[('my_data', ['data/data_file'])],

    # executable scripts
    #entry_points={
    #    'console_scripts': []
    #},

    cmdclass = {
        'clean': CleanCommand,
    },

)
