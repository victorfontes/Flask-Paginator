# -*- coding: utf-8 -*-
"""
Flask-Paginator
----------------

Simple pagination for flask apps
"""

from setuptools import setup

setup(
    name='Flask-Paginator',
    version='0.1',
    url='http://github.com/victorfontes/flask-paginator',
    license='BSD',
    author='Victor Fontes',
    author_email='contato@victorfontes.com',
    description='Simple pagination for Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
