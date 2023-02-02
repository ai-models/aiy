from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aiy",
    version="0.1",
    author="Justin Riddiough",
    author_email="contact@aimodels.org",
    description="A CLI assistant to get technical information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/author/aiy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE 2 License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "rich",
        "argparse",
        "platform",
        "sys",
        "resources",
        "condiut"
    ],
    entry_points={
        "console_scripts": [
            "aiy=aiy.main:main",
        ],
    },
)