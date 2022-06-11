
import sqlite3

conn = sqlite3.connect('misync.db',check_same_thread=False)
listofID=[]

def create_user(uname,mail,ph,city):
	curs = conn.cursor()
	curs.execute(f'insert into users values ({uname},{mail},1122334455,{city},null);')
	conn.commit()

def del_user(custid):
	curs=conn.cursor()
	curs.execute(f'delete from users where custid={custid}')
	conn.commit()


def update_user(specifier,val,custid):
	curs=conn.cursor()
	curs.execute(f'update users set {specifier}={val} where custid={custid};')
	conn.commit()

def count_custid():
	curs = conn.cursor()
	curs.execute(f'select custid from users;')
	conn.commit()
	for row in curs.fetchall():
		listofID.append(row[0])
	return listofID

def retrieve_user(id):
	curs=conn.cursor()
	user = curs.execute(f'select * from users where custid={id};')
	return user.fetchall()[0]

def retrieve_all():
	curs = conn.cursor()
	users = curs.execute(f'select * from users;')
	return users.fetchall()

def json_update():
	jdata = {}
	for i in listofID:
		user,mail,ph,ct = retrieve_user(i)
		jdata[i]['user']=user
		jdata[i]['mail']=mail
		jdata[i]['ph']=ph
		jdata[i]['city']=ct

	return jdata
