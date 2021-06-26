import os
import sqlite3

conn = sqlite3.connect('dsa.db')

cur = conn.cursor()


def create_table():
    
    cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, data TEXT,'\
        'prod_name TEXT, valor REAL)')
   


def data_insert():
    
    cur.execute("INSERT INTO produtos VALUES(10, '2025-05-02 14:00:01', 'Teclado', 90)")
    print("Inserido")
    conn.commit()
    
    conn.close()