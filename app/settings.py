import os
from urllib import quote_plus

DEBUG = True
HOST = '0.0.0.0'
DB_USER = os.environ.get('DB_USER', 'fractal')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'fractal@123')
DB_NAME = os.environ.get('DB_NAME', 'ds131997.mlab.com:31997/fractal')
# DB_USER = 'fractal_db_user'
# DB_PASSWORD = 'fractal_db_user'
# DB_NAME = '159.89.166.117:27017'
DB_URI = "mongodb://%s:%s@%s" % (quote_plus(DB_USER), quote_plus(DB_PASSWORD), DB_NAME)


TEMPLATES_DIR = 'templates'
STATIC_DIR = 'static'