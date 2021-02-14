from setuptools import setup, find_packages

setup(
    name='my_lib',
    version='0.1.0',
    requires=[
        'cowsay',
        'pytest',
        'flake8',
    ],
    packages=find_packages()
    # other parameters...
)
