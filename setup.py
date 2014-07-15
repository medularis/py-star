#!/usr/bin/env python

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
    author='Karl Putland',
    author_email='kputland@users.sourceforge.net',
    maintainer='Ralf Schlatterbeck',
    maintainer_email='rsc@runtux.com',
    url='http://www.sourceforge.net/projects/pyst/',
    packages=['py_star'],
    license='PSF, LGPL',
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
        'License :: OSI Approved :: Python Software Foundation License',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ]
)
