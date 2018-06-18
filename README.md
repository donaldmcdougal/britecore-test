# britecore-test
The test application for BriteCore
# Run instructions
1.  Run `virtualenv env` in the project's root folder in a terminal.
2.  `cd env`
3.  `source bin/activate`
4.  `pip install pybuilder`
5.  `pyb install_dependencies`
6.  `pyb`
7.  If you are still in the `env` folder, `cd ../src/main/python`
8.  `python seed.py` to generate seed data for clients and product areas.
9.  `python index.py` to start the application.  Navigate to [localhost:5000](http://localhost:5000/).
