import hashlib
import uuid


nome_usuario = input('entre com seu nome: ') 
palavra_chave = input('entre com sua senha: ')

# Criar um objeto de hash SHA-256
sha256 = hashlib.sha256()

# Adicionar dados ao objeto de hash
sha256.update(palavra_chave.encode('utf-8'))

# Obter o hash em formato hexadecimal
palavra_chave_com_hash = sha256.hexdigest()

usuario = {
  'nome': uuid.uuid1(),
  'senha': palavra_chave_com_hash
}

print(usuario['senha'])

print('LOGIN: ')
login_usuario = input('entre com seu nome: ')
login_senha = input('entre com sua senha: ')

# Criar um objeto de hash SHA-256
sha256 = hashlib.sha256()

# Adicionar dados ao objeto de hash
sha256.update(login_senha.encode('utf-8'))

# Obter o hash em formato hexadecimal
login_senha_com_hash = sha256.hexdigest()

if login_usuario == usuario['nome'] and login_senha_com_hash == usuario['senha']:
  print('login efetuado')
else:
  print('login nao efetuado')

'''
# String que queremos hashear
texto = "emile123"
texto1 = "94ae42a3c771dbc04ad674e628ec0f5a0891e1b21eae7ebf94e362393f1d20e4"

# Criar um objeto de hash SHA-256
sha256 = hashlib.sha256()

# Adicionar dados ao objeto de hash
sha256.update(texto.encode('utf-8'))

# Obter o hash em formato hexadecimal
hash_resultado = sha256.hexdigest()

if texto1 == hash_resultado:
  print('login efetuado')
else:
  print('login nao efetuado')

print("Senha original:", texto)
print("Senha com Hash SHA-256:", hash_resultado)
'''