"""
Flask-Paginator
----------------

Simple pagination for flask apps
"""

from setuptools import setup, find_packages

setup(
    name='Flask-Paginator',
    version='0.1',

    packages=['flaskext', 'flaskext.paginator'],
    namespace_packages=['flaskext'],

    url='http://github.com/victorfontes/flask-paginator',
    description='Simple pagination for Flask',
    long_description=__doc__,

    author='Victor Fontes',
    author_email='contato@victorfontes.com',
    license='BSD',
    
    #packages=['flaskext'],
    zip_safe=False, platforms='any',

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)




