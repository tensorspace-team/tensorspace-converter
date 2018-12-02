import os
import setuptools

from src import version

def _get_requirements(requirements_file_name):
    "Collect required packages from provided file"
    with open(os.path.join(os.path.dirname(__file__), requirements_file_name), 'r') as requirements:
        return requirements.readlines()


with open("README.md", "r") as fh:
    long_description = fh.read()

CONSOLE_SCRIPTS = [
    "tensorspace_converter = src.tsp_converters:main"
]

setuptools.setup(
    name="tensorspacejs",
    version=version.version,
    author="TensorSpace Team",
    author_email="tensorspaceteam@gmail.com",
    description="TensorSpace.js Python tool package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorspace-team/tensorspace-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: JavaScript",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

    install_requires=_get_requirements('requirements.txt'),
    entry_points={
        "console_scripts": CONSOLE_SCRIPTS
    },
    license="Apache 2.0",
    keywords="tensorspace javascript neural network 3d visualization converter"
)