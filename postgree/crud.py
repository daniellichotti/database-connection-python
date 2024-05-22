import psycopg2


# Configuração da conexão
def create_connection():
  conn = psycopg2.connect(
      dbname="usuarios",
      user="docker",
      password="docker",
      host="localhost",
      port="5432"
  )
  return conn

def create_table(table):
    conn = create_connection()
    # Criar um cursor para executar consultas
    cur = conn.cursor()

    # Exemplo de criação de tabela
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50),
            idade INTEGER
        )
    """)

    # Commit (confirmar) as alterações
    conn.commit()

    # Fechar o cursor e a conexão
    cur.close()

def drop_table(table):
    conn = create_connection()
    # Criar um cursor para executar consultas
    cur = conn.cursor()

    # Exemplo de criação de tabela
    cur.execute(f"""
        DROP TABLE IF EXISTS {table}
    """)

    print('Table deleted')

    # Commit (confirmar) as alterações
    conn.commit()

    # Fechar o cursor e a conexão
    cur.close()


def create_usuarios(nome, idade):
    conn = create_connection()
    # Criar um cursor para executar consultas
    cur = conn.cursor()
    
    # Exemplo de inserção de dados
    cur.execute("INSERT INTO usuarios (nome, idade) VALUES (%s, %s)", (nome, idade))

    # Commit (confirmar) as alterações
    conn.commit()  
    
    # Fechar o cursor e a conexão
    cur.close()

def read_users(table):
    conn = create_connection()
    # Criar um cursor para executar consultas
    cur = conn.cursor()

    # Exemplo de consulta SELECT
    cur.execute(f"SELECT * FROM {table}")

    usersList = []
    rows = cur.fetchall()
    for row in rows:
        usersList.append({
            'id': row[0],
            'nome': row[1],
            'idade': row[2]
        })
    # Fechar o cursor e a conexão
    cur.close()
    conn.close()
    
    return usersList

def update_usuarios(nome, idade):
    return

def delete_usuarios(user_id):
    conn = create_connection()
    # Criar um cursor para executar consultas
    cur = conn.cursor()

    # Exemplo de exclusão de dados de um usuário específico
    cur.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))

    # Commit (confirmar) as alterações
    conn.commit()

    # Fechar o cursor
    cur.close()

if __name__ == "__main__":
    table = 'usuarios'

    while 1:
        print("1 - Criar usuarios")
        print("2 - Ler usuarios")
        print("3 - Atualizar usuarios")
        print("4 - Deletar usuarios")
        print("5 - Sair")
        print("6 - Create Table")
        print("7 - Drop Table")
        
        opcao = int(input("Opção: "))

        if opcao == 1:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            create_usuarios(nome, idade)
        elif opcao == 2:
            read_users(table)
        elif opcao == 3:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            #update_usuarios(nome, idade)
        elif opcao == 4:
            user_id = int(input("User Id: "))
            delete_usuarios(user_id)
        elif opcao == 5:
            break
        elif opcao == 6:
            create_table(table)
        elif opcao == 7:
            drop_table(table)
        else:
            print("Opção inválida")
    
    

# Fechar o cursor e a conexão
#conn.close()


