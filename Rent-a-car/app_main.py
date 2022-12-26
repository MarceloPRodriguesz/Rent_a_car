# GET -> pesquisa
# PUT -> alteração
# DELETE -> exclusão
# POST -> inclusão
from flask import Flask, jsonify, request

app = Flask(__name__)

carros = []
clientes = []
locacoes = []

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


# ----- LOCAÇÃO DE VEICULOS

# Registrar locação
#  Adiciona nova locação
@app.route('/locacao', methods=['POST'])
def adicionar_locacao():
    nova_locacao = request.get_json()
    # Pego o ID do cliente para alteração 
    id_cliente = nova_locacao.get('id_cliente')
    id_carro = nova_locacao.get('id_carro')
    
    locacoes.append(nova_locacao)
    # Faço a alteração do Id através do método
    altera_status_cliente(id_cliente, True)
    altera_status_carro(id_carro, True)
    
    return jsonify(locacoes)

# Registrar devolução
@app.route('/locacao/<int:id>', methods=['DELETE'])
def excluir_locacao(id):
    for indice, locacao in enumerate(locacoes):
        if locacao.get('id') == id:
            id_cliente = locacao.get('id_cliente')
            id_carro = locacao.get('id_carro')
            altera_status_cliente(id_cliente, False)
            altera_status_carro(id_carro, False)
            del locacoes[indice]
            
    return jsonify(locacoes)

# Listando todas as locações
@app.route('/locacao', methods=['GET'])
def listar_locacoes():
    return jsonify(locacoes)  

#  Listar locações por id
@app.route('/locacao/<int:id>', methods=['GET'])
def listar_locacao_id(id):
    for locacao in locacoes:
        if locacao.get('id') == id:
            return jsonify(locacao)
                
def altera_status_cliente(id, status):
    status_atual = status
    
    if status_atual == True:
        status_atual = 'Possui locação'
        for indice, cliente in enumerate(clientes):
            if cliente.get('id_cliente') == id:
                clientes[indice]['status'] = status_atual
                
                return 
    else:
        status_atual = 'Nao possui locação'
        for indice, cliente in enumerate(clientes):
                     if cliente.get('id_cliente') == id:
                        clientes[indice]['status'] = status_atual
                        
                        return 
    
                                   
def altera_status_carro(id_carro, status):
    status_atual = status
    
    if status_atual == True:
        status_atual = 'Alugado'
        for indice, carro in enumerate(carros):
            if carro.get('id_carro') == id_carro:
                carros[indice]['status'] = status_atual
                return
    else:
        status_atual = 'Disponivel'
        for indice, carro in enumerate(carros):
                     if carro.get('id_carro') == id_carro:
                        carros[indice]['status'] = status_atual
                        return 
                
    

#  Executa a aplicação
app.run(port=5000, host='localhost', debug=True)