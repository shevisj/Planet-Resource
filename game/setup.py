from setuptools import setup, find_packages

setup(
    name='game',
    version='0.2',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=[
        'numpy>=1.18.4',
        'jsonpickle>=1.4.1',
    ],
    extras_require={
        'rendering': ['pygame>=1.9.6'],
        'test': ['pytest>=5.4.3'],
    }
)
