
import sys, os, logging
from app.settings import g_vars
from app.funcs import logs


logging.basicConfig(stream=sys.stderr)
sys.path.append(g_vars['main_path'])

logs.add_to_log("online start: path for root dir:" + str(g_vars['main_path']))

import app.includes
from app import app as application
