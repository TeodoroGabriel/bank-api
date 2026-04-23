import sqlite3
def conectar():
    conn = sqlite3.connect('banco.db')
    return conn
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT NOT NULL,
                          email TEXT NOT NULL UNIQUE,
                          senha TEXT NOT NULL,
                          cpf TEXT NOT NULL UNIQUE,
                          saldo REAL NOT NULL DEFAULT 0.0)''')
    conn.commit()
    conn.close()