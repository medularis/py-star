#!/usr/bin/env python

from distutils.core import setup

import py_asterisk


long_description = (
    "py-Asterisk consists of a set of interfaces and libraries to allow programming "
    "of Asterisk from python. The library currently supports AGI, AMI, "
    "and the parsing of Asterisk configuration files. The library also "
    "includes debugging facilities for AGI."
)

setup(
    name='py-Asterisk',
    version=py_asterisk.__version__,
    description='A Python Interface to Asterisk',
    long_description=long_description,
    author='German Larrain',
    author_email='glarrain@users.noreply.github.com',
    url='https://github.com/medularis/py-asterisk',
    packages=['py_asterisk'],
    license='PSF, LGPL',
    platforms='Any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Python Software Foundation License',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ]
)
