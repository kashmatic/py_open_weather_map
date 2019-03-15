"""
Setup tool for package pyopenweatherapp
"""
from setuptools import setup

setup(
    name="pyopenweatherapp",
    version="0.2.1",
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    dependency_links=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=['pyopenweatherapp'],
)
