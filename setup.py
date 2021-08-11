import setuptools
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='torch-kshingle-embedding',
    version=get_version("torch-kshingle-embedding/__init__.py"),
    description='Training of multi-label embeddings with k-shingled input sequences',
    long_description=read('README.rst'),
    url='http://github.com/ulf1/torch-kshingle-embedding',
    author='Ulf Hamster',
    author_email='554c46@gmail.com',
    license='Apache License 2.0',
    packages=['torch_kshingle_embedding'],
    install_requires=[
        "torch>=1.1.0,<2"
    ],
    python_requires='>=3.6',
    zip_safe=True
)
