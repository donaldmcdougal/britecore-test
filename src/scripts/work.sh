#!/bin/sh

cd ~
rm -rf britecore-test
git clone https://github.com/donaldmcdougal/britecore-test.git
cd britecore-test
virtualenv env
source env/bin/activate
pip install pybuilder
pyb install_dependencies
python src/main/python/index.py &
cd src/main/python
python minify.py
pyb
