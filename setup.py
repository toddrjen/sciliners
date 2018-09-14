# -*- coding: utf-8 -*-
#!/usr/bin/python3

from setuptools import setup, find_packages
from pathlib import Path

readme = (Path(__file__).parent / 'README.md')

setup(
    name="sciliners",
    version="0.0.1",
    author="Todd Jennings",
    author_email="toddrjen@gmail.com",
    description="Numeric, engineering, and science-oriented one-liners for python ",
    license="BSD-3-Clause",
    url="https://github.com/toddrjen/sciliners",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/toddrjen/sciliners/issues"
    }

    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3 :: Only',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 ],

    keywords='scipy numpy numeric scientific one-liner oneliner one-liners oneliners',

    install_requires=['numpy',
                      'scipy'],

    tests_require=['pytest',
                   'hypothesis']

    python_requires='>=3.5',

    long_description=readme.read_text(encoding='utf8'),
    long_description_content_type='text/markdown',

    packages=find_packages(),

    include_package_data=True,
)
