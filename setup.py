#!/usr/bin/env python
import sys
import os
from setuptools import setup, find_packages
from django_netjsongraph import get_version


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip to next iteration if comment or empty line
        if line.startswith('#') or line == '' or line.startswith('http') or line.startswith('git'):
            continue
        # add line to requirements
        requirements.append(line)
    return requirements


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel upload -s")
    args = {'version': get_version()}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name='django_netjsongraph',
    version=get_version(),
    license='MIT',
    author='Federico Capoano',
    author_email='nemesis@ninux.org',
    description='Django implementation of NetJSON NetworkGraph',
    url='http://netjson.org',
    download_url='https://github.com/interop-dev/django_netjsongraph/releases',
    platforms=['Platform Indipendent'],
    keywords=['django', 'netjson', 'mesh', 'networking'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=get_install_requires(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)