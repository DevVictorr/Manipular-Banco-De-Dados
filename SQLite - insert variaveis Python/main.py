import os
import sqlite3
import inserts as ins
import time
import datetime
import random

ins = ins

conn = sqlite3.connect('dsa.db')

cur = conn.cursor()

ins.create_table()

#ins.data_insert()


for i in range(5):
    ins.data_insert_var()
    time.sleep(1)

conn.close()

ins.dados_grafico()







