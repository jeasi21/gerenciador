import os
import sqlite3 



def conectar():
    arquivos = r"C:\akemi_database"
    if not os.path.exists(arquivos):
        os.makedirs(arquivos)
    banco_de_dados = os.path.join(arquivos, 'clientes.db')
    #return sqlite3.connect('./dados/clientes.db')
    return sqlite3.connect(banco_de_dados)

def criar_tabela():    
        try:
            with conectar() as conn:
                sql = '''CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, 
                tel TEXT, email TEXT, plano TEXT NOT NULL, vencimento TEXT NOT NULL)'''

                cursor = conn.cursor()
                cursor.execute(sql)
            
            print('Tabela Criada com sucesso!')
        except:
            print('Erro:Criação de tabela não concluido!')


def salvar_cliente(nome, tel, email, plano, vencimento):
    try:
        with conectar() as conn:
            dados_cliente = (nome, tel, email,plano, vencimento)
            sql = ' INSERT INTO usuarios(nome, tel,email, plano, vencimento) VALUES(?,?,?,?,?)'
            cursor = conn.cursor()
            cursor.execute(sql,dados_cliente)
        
        message ='Usuario salvo com sucesso!'
    except:
        message = "ERRO: Dados não inseridos!"
    return message


def exibir_clientes():
  
        with conectar() as conn:
            sql = 'SELECT * FROM usuarios'
            cursor = conn.cursor()
            cursor.execute(sql)
            cliente = cursor.fetchall()
        return cliente

def excluir_cliente(id ):
    
    with conectar() as conn:
        sql = 'DELETE FROM usuarios WHERE id=?'
        cursor = conn.cursor()
        cursor.execute(sql,(id,))
        conn.commit()
       

def atualizar_cliente(id, nome, tel, email, plano, vencimento):
    with conectar() as conn:
        sql = 'UPDATE usuarios SET nome=? , tel=? , email=? , plano=?, vencimento=? WHERE id=? '
        cursor = conn.cursor()
        cursor.execute(sql,(nome, tel, email, plano, vencimento, id,))
        conn.commit()
       
def buscar_cliente(nome):
    with conectar() as conn:
        sql = 'SELECT id, nome, tel, email, plano, vencimento FROM usuarios WHERE nome LIKE ?'
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{nome}%',))
        cliente = cursor.fetchall()
    return cliente
     

     

conectar()
criar_tabela()
#print(exibir_clientes())


#salvar_cliente('maria2', '98765-4456', 'maria@gmail.com', '40mbps', 'dia 10')

   
