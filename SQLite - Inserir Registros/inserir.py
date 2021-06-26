import os
import sqlite3

con = sqlite3.connect('escola.db')

cur = con.cursor()#

sqlite3_insert = 'insert into cursos values(?,?,?)'
sqlite3_select = 'select * from cursos'


recset = [(1000, 'Ciencia de Dados',     'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos',   'Analise de Dados')]
        

for rec in recset:
    cur.execute(sqlite3_insert, rec)

con.commit()


