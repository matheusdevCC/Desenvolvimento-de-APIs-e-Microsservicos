from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []
proximo_id = 1 

@app.route('/users', methods=['POST'])
def criar_usuario():
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

    return jsonify(novo_usuario), 201  # Retorna o usuário criado com status 201

@app.route('/users', methods=['GET'])

def retorna_usuario():
    return jsonify(usuarios)

@app.route('/users/<int:id>', methods=['GET'])
def retorna_usuario_id(id):
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
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': f'Usuário {id} removido com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404        

if __name__ == '__main__':
    app.run(debug=True)