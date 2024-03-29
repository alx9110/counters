""" Setup """
from os.path import join, dirname
from setuptools import setup, find_packages


requirements = [
    
]

setup(
    name='counters',
    version='0.1',
    author='Alexander Telkov',
    author_email='alx9110@yandex.ru',
    install_requires=requirements,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    test_suite='tests',
)
