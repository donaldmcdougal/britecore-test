# britecore-test
The test application for BriteCore
# Run instructions
1.  Run `virtualenv env` in the project's root folder in a terminal.
2.  `cd env`
3.  `source bin/activate`
4.  `pip install flask`
5.  `pip install sqlalchemy`
6.  `pip install python-dateutil`
7.  If you are still in the `env` folder, `cd ..`
8.  `python seed.py` to generate seed data for clients and product areas.
9.  `python index.py` to start the application.  Navigate to [localhost:5000](http://localhost:5000/).
