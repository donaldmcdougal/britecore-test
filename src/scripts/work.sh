#!/bin/sh

APP_DIR=/root/britecore-test
GIT_URL=https://github.com/donaldmcdougal/britecore-test
RESTART_ARGS="--port 5000"

set -x

cd $APP_DIR
git pull
cd britecore-test
virtualenv env
source env/bin/activate
pip install pybuilder
pyb install_dependencies
cd src/main/python
python minify.py
cd ../../../../
# Restart app
passenger-config restart-app --ignore-app-not-running --ignore-passenger-not-running $RESTART_ARGS $APP_DIR

# python src/main/python/index.py &
#
# python minify.py
# pyb
