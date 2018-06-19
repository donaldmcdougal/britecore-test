# britecore-test
John Schneider's test application for BriteCore.

For simplicity, all the python files are in src/main/python.  Also for simplicity,
AJAX calls are nested rather than using promises.

# Run instructions
1.  Run `apt install virtualenv` if virtualenv is not already installed.
2.  Run `virtualenv env` in the project's root folder in a terminal.
3.  `source env/bin/activate`
4.  `pip install pybuilder`
5.  `pyb install_dependencies`
6.  `pyb`
7.  `cd src/main/python`
8.  `python minify.py`
9.  `python index.py` to start the application.  Navigate to [localhost:5000](http://localhost:5000/).
