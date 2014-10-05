from datetime import timedelta, datetime
import json, os
from flask import send_from_directory

from app import app
from app.funcs import db_work, logs, generators

from app.settings import g_vars

@app.route('/static/images/<files>')
def get_img(files):
	return send_from_directory(g_vars['static_images_path'], files)