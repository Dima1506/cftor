#*-* coding: utf-8 *-*

import dataset
db = dataset.connect('mysql://ghjvfy1999:ghjvfy1506@ghjvfy1999.mysql.pythonanywhere-services.com/ghjvfy1999$fas')
table = db["users"]

def isLogin(login_t):
	if(None == table.find_one(login  = login_t)):
		return 0
	else:
		return 1

def isPasswd(login_t, passwd_t):
	if(table.find_one(login = login_t)["passwd"] == passwd_t):
		return 1
	else:
		return 0


def regino(name, email_t, passwd_t):
    if(None != table.find_one(login = login_t)):
        table.insert(dict(login = email_t, passwd=passwd_t, fio=name, role = int(0), number = int(8999)))


def name(login_t):
	return [table.find_one(login = login_t)["name"], table.find_one(login = login_t)["last_name"]]


print(isLogin(1))








