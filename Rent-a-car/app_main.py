# GET -> pesquisa
# PUT -> alteração
# DELETE -> exclusão
# POST -> inclusão
from flask import Flask, jsonify, request

app = Flask(__name__)

carros = []
clientes = []

#  ----- MÉTODOS CARRO ----------
#  Adiciona novo carro
@app.route('/carros', methods=['POST'])
def adicionar_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(carros)

#  Editando carros
#  Função recebe valor digitado pelo usuario, verifica qual cadastro sera
# editado através de laço de repetição e efetua a alteração.
@app.route('/carros/<int:id>', methods= ['PUT'])
def editar_carro(id):
    carro_editado = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_editado)
            return jsonify(carros[indice])
        
#  Deletando carros
#  Função pesquisa cadastro do veiculo, verifica atraves de laço 
#de repetição e faz a exclusão do mesmo assim que o encontrar.
@app.route('/carros/<int:id>', methods= ['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
            
    return jsonify(carros)
    
# Listando todos os carros
@app.route('/carros', methods=['GET'])
def listar_carros():
    return jsonify(carros)    

#  Listar carro por id
@app.route('/carros/<int:id>', methods=['GET'])
def listar_carros_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)


# ----- MÉTODOS CLIENTE -----

#  Adicionando novo cliente
@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_clientes(id):
    cliente_editado = request.get_json()
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_editado)
            return jsonify(clientes[indice])
        
#  Deletando clientes
@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_clientes(id):
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]
            
    return jsonify(clientes)
    

# Listando todos os clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)  

#  Listar cliente por id
@app.route('/clientes/<int:id>', methods=['GET'])
def listar_clientes_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)



#  Executa a aplicação
app.run(port=5000, host='localhost', debug=True)