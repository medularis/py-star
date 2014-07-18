#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import py_star


long_description = (
    "py-star consists of a set of interfaces and libraries to allow programming "
    "of Asterisk from python. The library currently supports AGI, AMI, "
    "and the parsing of Asterisk configuration files. The library also "
    "includes debugging facilities for AGI."
)

setup(
    name='py-star',
    version=py_star.__version__,
    description='A Python Interface to Asterisk',
    long_description=long_description,
    author='German Larrain',
    author_email='glarrain@users.noreply.github.com',
    url='https://github.com/medularis/py-star',
    packages=['py_star'],
    license='3-clause BSD',
    platforms='Any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # the FSF refers to it as "Modified BSD License". Other names include
        # "New BSD", "revised BSD", "BSD-3", or "3-clause BSD"
        'License :: OSI Approved :: BSD License',
    ]
)
