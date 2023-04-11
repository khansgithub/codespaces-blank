#!/bin/bash
# TODO: replace with cookiecutter

ROOT=/workspaces/codespaces-blank

if [ "$(pwd)" = $ROOT ]; then
  :
else
  echo "Error: current directory is NOT $ROOT"
  exit 1
fi

if [ $# -eq 0 ]
  then
    echo "Error: Missing parameter"
    echo "Usage: $0 <parameter>"
    exit 1
fi

cd mod
mkdir $1
cd $1

touch setup.py
touch __init__.py

cat << EOF > setup.py
from setuptools import setup, find_packages

setup(
    name='',
    version='0.1.0',
    description='',
    author='',
    author_email='',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
)
EOF

cat << EOF > requirements.txt
setuptools
wheel
rq
redis
EOF

python3 -m venv .
source ./bin/activate
pip3 install -r requirements.txt