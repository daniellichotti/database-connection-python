from pymongo import MongoClient

# Configuração da conexão
client = MongoClient("mongodb://docker:docker@localhost:27017/")
db = client["usuarios"]

usuarios = db.usuarios  # coleção 'usuarios' dentro do banco de dados 'usuarios'

def create_usuarios(nome, idade, profissao):
    # Inserir um novo documento na coleção
    usuarios.insert_one({"nome": nome, "idade": idade, "profissao": profissao})

def read_users():
    # Ler todos os documentos na coleção
    for user in usuarios.find():
        print(user)

def delete_usuarios(user_id):
    # Deletar um documento pela sua chave '_id'
    usuarios.delete_one({"_id": user_id})

def update_usuarios(user_id, nome, idade):
    # Atualizar um documento
    usuarios.update_one({"_id": user_id}, {"$set": {"nome": nome, "idade": idade}})

if __name__ == "__main__":
    while True:
        print("1 - Criar usuários")
        print("2 - Ler usuários")
        print("3 - Atualizar usuários")
        print("4 - Deletar usuários")
        print("5 - Sair")
        
        opcao = int(input("Opção: "))
        if opcao == 1:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            profissao = input("profissao: ")
            create_usuarios(nome, idade, profissao)
        elif opcao == 2:
            read_users()
        elif opcao == 3:
            user_id = input("User ID: ")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            update_usuarios(user_id, nome, idade)
        elif opcao == 4:
            user_id = input("User ID: ")
            delete_usuarios(user_id)
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
