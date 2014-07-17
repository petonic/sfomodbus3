"""
Installs pymodbus using distutils

Run:
    python setup.py install
to install the package from the source archive.

For information about setuptools
http://peak.telecommunity.com/DevCenter/setuptools#new-and-changed-setup-keywords
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys
import os
from setup_commands import command_classes
from pymodbus3 import __version__, __author__, __author_email__


def main():
    # Check python version
    if sys.version_info < (3, 0, 0):
        sys.stderr.write('You need python 3.0 or later to run this script!' + os.linesep)
        exit(1)
    setup(
        name='pymodbus3',
        version=__version__,
        description='A fully featured modbus protocol stack in python',
        long_description=open('README.rst').read(),
        keywords='modbus, twisted, scada',
        author=__author__,
        author_email='bashwork@gmail.com',
        maintainer=__author__,
        maintainer_email=__author_email__,
        url='https://github.com/uzumaxy/pymodbus3',
        license='BSD',
        packages=['pymodbus3'],
        exclude_package_data={'': ['examples', 'test', 'tools', 'doc']},
        platforms=['Linux', 'Mac OS X', 'Win'],
        include_package_data=True,
        zip_safe=True,
        install_requires=[
            'twisted >= 12.2.0',
            'pyserial >= 2.6'
        ],
        extras_require={
            'quality': ['coverage >= 3.5.3', 'nose >= 1.2.1', 'mock >= 1.0.0', 'pep8 >= 1.3.3'],
            'documents': ['sphinx >= 1.1.3'],
            'twisted': ['pyasn1 >= 0.1.4', 'pycrypto >= 2.6'],
        },
        test_suite='nose.collector',
        cmdclass=command_classes,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: X11 Applications :: GTK',
            'Environment :: MacOS X',
            'Environment :: Win32 (MS Windows)',
            'Framework :: Twisted',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows :: Windows 7',
            'Operating System :: Microsoft :: Windows :: Windows NT/2000',
            'Operating System :: Microsoft :: Windows :: Windows Server 2003',
            'Operating System :: Microsoft :: Windows :: Windows Server 2008',
            'Operating System :: Microsoft :: Windows :: Windows Vista',
            'Operating System :: Microsoft :: Windows :: Windows XP',
            'Operating System :: Microsoft',
            'Operating System :: OS Independent',
            'Operating System :: POSIX :: BSD :: FreeBSD',
            'Operating System :: POSIX :: Linux',
            'Operating System :: POSIX :: SunOS/Solaris',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Libraries',
            'Topic :: System :: Networking',
            'Topic :: System :: Networking :: Monitoring',
            'Topic :: Utilities'
        ],
    )


if __name__ == '__main__':
    main()
