from flask import *
import requests
import sqlite3
from dbcon import *
app = Flask(__name__)

total_user = count_custid()
@app.route('/home')
def home():
	return "Welcome to Game of API"

@app.route('/home/delete/<int:id>',methods=['GET','POST','PUT','DELETE'])
def delete_user(id):
	if request.method == 'DELETE' or request.method=='GET':
		total_user = count_custid()
		if id in total_user:
			del_user(id)
			return "User deleted from database"
		else:
			return "Not Valid UserID!!!"
	else:
		return "NOT Valid Request!!!",401

@app.route('/home/create',methods=['POST','GET'])
def create():
	if request.method == 'POST':
		total_user = count_custid()
		user=request.args.get('user')
		mail=request.args.get('mail')
		phone= request.args.get('ph')
		city=request.args.get('city')
		create_user(user,mail,phone,city)
		return f"User created with name {user} and userid{total_user[-1]+1}"
	else:
		return "Make it Post Req!!!",401

@app.route('/home/view',methods=['GET'])
def retrieve():
	id = request.args.get('id')
	if id:
		l = retrieve_user(id)
		user , mail , ph,city,id = l[0],l[1],l[2],l[3],l[4]
		return 	f'User:{user}<br>Mail:{mail}<br>phone:{ph}<br>city:{city}<br>id:{id}'
	else:
		l = retrieve_all()
		s = ""
		for i in l:
			s+=	 str(i)+'<br>'
		return s


@app.route('/home/update',methods=['PUT','GET','POST'])
def update():
	if request.method=='PUT' or request.method=='POST':
		specifier = request.args.get('spec')
		val = request.args.get('val')
		id = request.args.get('id')
		update_user(specifier,val,id)
		return "Updated!!"
	else:
		return "ITs an UPDATE!! Make it PUT request",401
