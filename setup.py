import os
from setuptools import find_packages, setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# This call to setup() does all the work
setup(
    name="pypokemontcg",
    version="0.0.0",
    description="SDK for pokemontcg APIs",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/eduardo-prjadko/pypokemontcg.git",
    author="Eduardo Prjadko",
    author_email="eduardoabp@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",))
)