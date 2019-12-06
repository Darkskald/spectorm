from setuptools import setup, find_packages

with open("README.md", "r") as infile:
    long_description = infile.read()

setup(
    name="spectorm",
    version="0.0.1",
    author="Florian-David Lange",
    author_email="lange@phc.uni-kielde",
    description="An extensible toolset for spectral data handling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Darkskald/spectorm",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "sqlalchemy",
        "pandas",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)