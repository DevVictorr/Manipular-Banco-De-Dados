import os
import sqlite3
import inserts as ins

ins = ins

conn = sqlite3.connect('dsa.db')

cur = conn.cursor()

#ins.create_table()

ins.data_insert()

