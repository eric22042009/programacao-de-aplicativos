import sqlite3

nome_banco = ("gestao_escolar.db")

def conectar():
    conexao = sqlite3.connect(nome_banco)
    conexao.execute ("PRAGMA foreing_keys = ON;")
    return conexao

def criar_tabelas():
    try:
        conexao = conectar()
        cursor.