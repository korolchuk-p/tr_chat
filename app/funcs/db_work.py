import MySQLdb
from app.settings import g_vars

def db_con():
	return MySQLdb.connect(host=g_vars['mysql_server'], 
                     user=g_vars['mysql_user'], 
                      passwd=g_vars['mysql_passwd'],
                      db=g_vars['mysql_database']) 



def add_mes(author, text):

	db = db_con()
	cur = db.cursor()

	cur.execute("INSERT INTO `messages` (`author`, `text`) VALUES ('{0}', '{1}')".format(author, text))

	db.commit()
	cur.close()
	db.close()

	return 1

def to_utf8(obj):
	return obj.encode('utf-8') 

def get_mes(lasts=0):
	db = db_con()
	cur = db.cursor()

	if lasts:
		cur.execute("SELECT * FROM (SELECT * FROM  `messages` ORDER BY id DESC LIMIT {0}) AS `table` ORDER BY id ASC".format(str(lasts)))
	else:
		cur.execute("SELECT * FROM `messages`")

	res=((row[0], row[1].decode('utf8'), row[2].decode('utf8')) for row in cur.fetchall())

	cur.close()
	db.close()	

	return res

