import sqlite3 

def cadastrar_escola_manual():
    id_escola = int(input("digite o ID para a nova escola: "))
    nome = input("nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

   