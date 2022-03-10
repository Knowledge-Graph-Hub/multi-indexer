import os

from codecs import open as copen  # to use a consistent encoding
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# get the long description from the relevant file
with copen(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

__version__ = "0.0.3"

test_deps = [
    'pytest',
    'pytest-cov',
    'coveralls',
    'validate_version_code',
    'codacy-coverage',
    'parameterized'
]

extras = {
    'test': test_deps,
}

setup(
    name='multi-indexer',
    version=__version__,
    description='A utility for creating sets of templated indexes for local or remote directories.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Knowledge-Graph-Hub/multi-indexer',
    author='Harry Caufield',
    author_email='',
    python_requires='>=3.7',

    # choose your license
    license='BSD-3',
    include_package_data=True,
    classifiers=[],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # add package dependencies
    install_requires=[
        'boto3',
        'pystache', 
    ],
    extras_require=extras,
)
