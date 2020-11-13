#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bbw",
    version="0.1",
    author="Renat Shigapov, Philipp Zumstein, Jan Kamlah, Lars Oberlaender, Joerg Mechnich, Irene Schumm",
    license="MIT",
    description="Library for semantic annotation of tabular data with the Wikidata knowledge graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UB-Mannheim/bbw",
    python_requires=">=3.6",
    install_requires=[
	ftfy>=5.8,
	tqdm>=4.48.0,
	pandas>=1.0.5,
	requests>=2.23.0,
	numpy>=1.18.4,
	beautifulsoup4>=4.9.3,
    ]
    packages=setuptools.find_packages(),
    classifiers=[
	"License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
	"Intended Audience :: Education",
        "Intended Audience :: Science/Research",
	"Operating System :: OS Independent",
	"Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
	"Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)