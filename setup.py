# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='emailmeform',
    version='0.1',
    description='Simple cloud hosted API to send forms to email',
    url='http://github.com/istinspring/sendmeform',
    author='Alex Istinspring',
    author_email='istinspring@gmail.com',
    license='GPLv3',
    packages=['emailmeform'],
    install_requires=[
        'uvloop',
        'aiodns',
        'cchardet',
        'aiohttp',
        'aiohttp-swagger[performance]',
        # extra
        'pylint',
        'flake8'
    ],
    zip_safe=False
)
