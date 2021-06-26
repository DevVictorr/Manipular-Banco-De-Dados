import os
import sqlite3
import datetime
import random
import matplotlib.pyplot as plt

conn = sqlite3.connect('dsa.db')

cur = conn.cursor()


def create_table():
    
    cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'\
        'prod_name TEXT, valor REAL)')
   


def data_insert():
    
    cur.execute("INSERT INTO produtos VALUES(10, '2025-05-02 14:00:01', 'Rebanho', 90)")
    print("Inserido")
    conn.commit()
    
    


def data_insert_var():

    new_date = datetime.datetime.now()
    new_prod_name = 'Cadeira'
    new_valor = random.randrange(50,100)
    cur.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?,?,?)", (new_date,new_prod_name,new_valor))
    conn.commit()

def atualiza_dados():

    cur.execute('UPDATE produtos SET valor = 70.00 WHERE valor = 80.0')
    conn.commit()

def remove_dados():
    cur.execute('DELETE FROM produtos WHERE valor = 60.0')
    conn.commit()

def dados_grafico():
    cur.execute('SELECT id, valor FROM produtos')
    ids = []
    valores = []

    dados = cur.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids,valores)
    plt.show()



