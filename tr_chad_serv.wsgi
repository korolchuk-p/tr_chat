
import sys, os, logging
from app.settings import g_vars

logging.basicConfig(stream=sys.stderr)
sys.path.append(g_vars['main_path'])


from app import app as application
