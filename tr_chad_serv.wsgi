
import sys, os, logging
from app.settings import *

#from tr_chad import app as application #<- app

logging.basicConfig(stream=sys.stderr)
sys.path.append(g_vars['main_path'])

from app import app as application #<- app
