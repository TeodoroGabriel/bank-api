from flask import Flask, request, jsonify
from database import criar_tabela, conectar

app = Flask(__name__)
criar_tabela()

@app.route("/")
def home():
    return "Banco Rodando!"

@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.get_json()

    cpf = dados.get("cpf")
    email = dados.get("email")
    senha = dados.get("senha")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (cpf, email, senha) VALUES (?, ?, ?)", (cpf, email, senha))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuario Cadastrado!"})


print("iniciando servidor")
app.run(debug=True)