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
6.  In a separate terminal, run `python src/main/python/index.py`
7.  `python src/main/python/minify.py`
8.  `pyb`
9.  Kill the process in the separate terminal where you ran `python src/main/python/index.py`
10. `python src/main/python/index.py` to start the application.  Navigate to [localhost:5000](http://localhost:5000/).
