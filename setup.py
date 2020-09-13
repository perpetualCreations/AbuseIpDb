# copied straight from https://packaging.python.org/tutorials/packaging-projects/
# Authors are left blank, I don't want to use someone else's identity, but I didn't make any major edits to the source code either to justify changing it to my own credentials.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abuseipdb",
    version="2.0.2", # According to the original repo, the last version was 2.0.1, I swept everything since into 2.0.2
    author="",
    author_email="",
    description="Wrapper for AbuseIPDB API, originally made by vsecades (https://github.com/vsecades/).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perpetualCreations/AbuseIPDB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)