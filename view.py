import sqlite3 as lite

#criando conexão
con = lite.connect('dados.db')

'''
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENTE mone TEXT)')
'''
 
# Inserir informações 
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO formulario (nome, origem, mês, valor) VALUES(?, ?, ?, ?)'
        cur.execute(query, i)



# Acessar informações 
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = 'SELECT* FROM formulario'
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista


# Atualizar informações 

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE formulario SET nome=?, origem=?, mes=?, valor=?'
        cur.execute(query, i)


# Deletar  informações 

def deletar_info(i):

    with con:
        cur = con.cursor()
        query = 'DELETE FROM formulario WHERE nome=("KJSANK")'
        cur.execute(query, i)

