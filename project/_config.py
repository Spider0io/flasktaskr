import os

#grab the folder where thsi script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENANLED = True
SECRET_KEY = 'my_precious'

#define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
