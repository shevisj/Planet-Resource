from setuptools import setup, find_packages

setup(
    name='game',
    version='0.1',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=[
        'numpy>=1.18.4',
        'jsonpickle==1.4.1',
        'nose==1.3.7'
    ]
)
