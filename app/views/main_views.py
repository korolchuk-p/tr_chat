# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, session, url_for, jsonify
from datetime import timedelta, datetime
import json

from app import app
from app.funcs import db_work, logging, generators




@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=str(a + b) + str(" <-ololo"))


@app.route('/')
def index():
    if 'date' not in session:
        session['date']=datetime.now()
    if 'token' not in session:
        session['token']=generators.get_rand_hex(32)
        logging.add_to_log("give rnd token: " + str(session['token']))
    date = session['date']
    mes=db_work.get_mes(0)
    return render_template('index.html', date1=date, mess=mes)


@app.route('/add', methods=['POST', 'GET'])
def add_mes():
    logging.add_to_log("receive method:" + request.method)
    if request.method=="GET" : return "ololo"
    author=request.form.get('author', "").encode('utf-8')
    mes=request.form.get('mes', "").encode('utf-8')#.decode('utf-8')

    logging.add_to_log("mes = " + str(mes))
    logging.add_to_log("author = " + str(author))


    if author and mes:
        db_work.add_mes(author, mes)
        res = { 
            'success': 'true' 
             }
    else:
        res = { 
        'success': 'false' 
         }



    logging.add_to_log("res = " +str(res))
    return  json.dumps(res)









