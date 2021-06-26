import os
import sqlite3

con = sqlite3.connect('escola.db')

cur = con.cursor()


sqlite3.create = 'create table cursos' \
             '(id integer primary key,' \
             'titulo varchar(100),'\
             'categoria varchar(125))'

cur.execute(sqlite3.create)

