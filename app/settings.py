from urllib import quote_plus

DEBUG = True

DB_NAME = 'test'
DB_USER = 'fractal'
DB_PASSWORD = 'fractal@123'
DB_URI = "mongodb://%s:%s@%s" % (
    quote_plus('fractal'), quote_plus('fractal@123'), 'ds131997.mlab.com:31997/fractal')


TEMPLATES_DIR = 'templates'
STATIC_DIR = 'static'
