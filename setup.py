# setup.py
from setuptools import setup, find_packages

setup(
    name="crypto-utils",
    version="0.1.0",
    packages=find_packages(),  
    install_requires=[
        "cryptography",
        "argon2-cffi"
    ],
)
