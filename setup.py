import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-blockstack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'blockchainauth>=0.3.1',
        'blockstack-profiles>=0.14.1',
        'django>=1.11'
        'PyJWT>=1.5.0',
    ],
    include_package_data=True,
    license='MIT',
    description='Django application that enables Blockstack-based authentication for your website.',
    long_description=README,
    keywords='blockstack django blockchain auth authentication id identity login bitcoin cryptocurrency',
    url='https://github.com/spankratov/django-blockstack/',
    author='Stanislav Pankratov',
    author_email='ss-pankratov@yandex.ru',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)