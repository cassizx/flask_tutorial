from os import name
from setuptools import _install_setup_requires, find_packages, setup, version

setup(
    name='flaskr',
    version='1.0.1',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'coverage',
        'flask',
        'flask-cli',
        'gunicorn',
        'pytest',
    ],
)