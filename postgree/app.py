from flask import Flask, request
from flask_cors import CORS
from crud import read_users, create_usuarios

app = Flask(__name__)
CORS(app)

@app.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    
    create_usuarios(data['nome'], data['idade'])
    return {'message': f'Usuario {data["nome"]} criado com sucesso'}

@app.route("/users", methods=['GET'])
def list_users():
    users = read_users('usuarios')
    print(users)
    return users


if __name__ == "__main__":
    app.run(debug=True)