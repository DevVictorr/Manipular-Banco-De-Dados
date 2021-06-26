import os
import sqlite3

con = sqlite3.connect('escola.db')

cur = con.cursor()


sqlite3_select = 'select * from cursos'


cur.execute(sqlite3_select)
dados = cur.fetchall()

for linha in dados:
    print('Id: %d, Curso: %s, Categoria: %s' %linha)