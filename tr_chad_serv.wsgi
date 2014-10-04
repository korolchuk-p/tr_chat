
import sys, os, logging

sys.path.append('C:/wamp/www/tr_chad')

logging.basicConfig(stream=sys.stderr)


from app import app as application

import app.includes

from app.funcs import logs
from app.settings import g_vars

