import os
if os.environ.get('DATABASE_URL'):
    DATABASE_PATH = os.environ['DATABASE_URL']
else:
    DATABASE_PATH = 'sqlite:///linkme.db'
SECRET_KEY = 'secret'
DEBUG = False 
