import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'nodeping_api'
DESCRIPTION = 'Python package for querying the NodePing API'
URL = 'https://github.com/NodePing/python3-nodeping-api'
EMAIL = 'support@nodeping.com'
AUTHOR = 'NodePing'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '0.9.1'
LICENSE = 'MIT'

REQUIRED = [
    'json', 'sys', 'urllib.error', 'urllib.request'
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
