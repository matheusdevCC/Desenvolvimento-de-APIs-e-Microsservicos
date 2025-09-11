from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)

swagger = Swagger(app)

usuarios = []
proximo_id = 1 

@app.route('/users', methods=['POST'])
def criar_usuario():
    """
    Endpoint para criar um usuário novo
    ---
    responses:
      201:
        description: Usuário criado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                nome:
                  type: string
                  example: João
                email:
                  type: string
                  example: joao@example.com
    """
    dados = request.json

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'Erro: Não existe os campos solicitados dos parametros'}), 400
    
    global proximo_id
    novo_usuario = {
        'id': proximo_id,
        'nome': dados['nome'],
        'email': dados['email']
    }
    usuarios.append(novo_usuario)
    proximo_id +=1

    return jsonify(novo_usuario), 201  

@app.route('/users', methods=['GET'])
def retorna_usuario():
    """
    Endpoint para retornar todos os usuários
    ---
    responses:
      200:
        description: Lista de usuários retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  nome:
                    type: string
                    example: João
    """
    return jsonify(usuarios)

@app.route('/users/<int:id>', methods=['GET'])
def retorna_usuario_id(id):
    """
    Endpoint para retornar usuário com base no ID que foi passado como parametro
    ---
    responses:
      200:
        description: usuário encontrado com o parametro ID.
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                nome:
                  type: string
                  example: João
    """
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario) 
        return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:id>', methods=['PUT'])
def atualiza_usuario(id):
    dados = request.json
    for usuario in usuarios:
        if usuario['id'] == id:
            if 'nome' in dados:
                usuario['nome'] = dados['nome']
            if 'email' in dados:
                usuario['email'] = dados['email']
            return jsonify(usuario),200

    return jsonify({'erro': 'usuário não encontrado.'})        

@app.route('/users/<int:id>', methods=['DELETE'])
def exclui_usuario(id):
    """
Endpoint para excluir usuário com base no ID que foi passado como parametro
---
responses:
  200:
    description: usuário encontrado com o parametro ID e excluido com sucesso.
    content:
      application/json:
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João
  404:
    description: Usuário não encontrado
    content:
      application/json:
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
"""
    
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': f'Usuário {id} removido com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404        

if __name__ == '__main__':
    app.run(debug=True)