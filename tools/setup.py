# setup.py
from setuptools import setup, find_packages

setup(
    name='devtool',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'typer',
    ],
    entry_points='''
        [console_scripts]
        devtool=devtool.devtool:app
    ''',
)