import os

from setuptools import setup


def read(f):
    here = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(here, f), encoding='utf-8').read().strip()


setup(
    name='djed.testing',
    version='0.2.dev0',
    description='Base unit test case for Pyramid',
    long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
    classifiers=[
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
    author='Djed developers',
    author_email='djedproject@googlegroups.com',
    url='https://github.com/djedproject/djed.testing',
    license='ISC License (ISCL)',
    keywords='web pyramid pylons djed',
    packages=['djed'],
    include_package_data=True,
    install_requires=[
        'pyramid',
        'nose',
        'webtest',
    ],
    extras_require={
        'testing': [],
    },
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
        ],
    },
)
