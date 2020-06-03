# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-nirmal",  # the name that you will install via pip
    version="1.6",
    author="Nirmal Thapa",
    author_email="nirmal-thapa@lambdastudents.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/nimu77/lambdata-nirmal",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
