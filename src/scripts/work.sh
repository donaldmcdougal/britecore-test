#!/bin/sh

git clone https://github.com/donaldmcdougal/britecore-test.git
cd britecore-test
virtualenv env
source env/bin/activate
pip install pybuilder
pyb install_dependencies
python src/main/python/index.py &
python src/main/python/minify.py
pyb
