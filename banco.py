import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')


# Criando tabela 
with con:
    cur = con.cursor()
    cur.execute('create table formulario (NOME TEXT, ORIGEM TEXT, MêS TEXT, VALOR FLOAT)')

