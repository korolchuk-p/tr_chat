import MySQLdb
#from app.settings import g_vars


g_vars=dict()

g_vars['mysql_passwd'] = "shit8529"
g_vars['mysql_user'] = "root"
g_vars['mysql_database'] = "test1"
g_vars['mysql_server'] = "localhost"


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


def get_mes(lasts=0):
	db = db_con()
	cur = db.cursor()

	if lasts:
		cur.execute("SELECT * FROM (SELECT * FROM  `messages` ORDER BY id DESC LIMIT {0}) AS `table` ORDER BY id ASC".format(str(lasts)))
	else:
		cur.execute("SELECT * FROM `messages`")

	res=((row[0], row[1], row[2]) for row in cur.fetchall())

	cur.close()
	db.close()	

	return res


add_mes("Kseniya","pashyk good! Trololo")

# for x in get_mes(0):
# 	print x