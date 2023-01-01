from flask import Flask, jsonify, request
from datetime import *

app = Flask(__name__)

carros = []
clientes = []
locacoes = []

#  ----- MÉTODOS CARRO ----------
@app.route('/carros', methods=['POST'])
def adicionar_carro():
    '''Adiciona novo veículo'''
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(carros)

@app.route('/carros/<int:id>', methods= ['PUT'])
def editar_carro(id):
    '''Edita informações de um veiculo passado por parametro'''
    carro_editado = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id_carro') == id:
            carros[indice].update(carro_editado)
            return jsonify(carros[indice])
        
@app.route('/carros/<int:id>', methods= ['DELETE'])
def excluir_carro(id):
    '''Deleta um veiculo passado por parametro'''
    for indice, carro in enumerate(carros):
        if carro.get('id_carro') == id:
            del carros[indice]
            
    return jsonify(carros)
    
@app.route('/carros', methods=['GET'])
def listar_carros():
    '''Exibe todos os veículos registrados'''
    return jsonify(carros)    

@app.route('/carros/<int:id>', methods=['GET'])
def listar_carros_id(id):
    '''Exibe veículo por parametro'''
    for carro in carros:
        if carro.get('id_carro') == id:
            return jsonify(carro)


# ----- MÉTODOS CLIENTE -----
@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    '''Adiciona novo cliente'''
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_clientes(id):
    '''Edita cliente por parametro'''
    cliente_editado = request.get_json()
    for indice, cliente in enumerate(clientes):
        if cliente.get('id_cliente') == id:
            clientes[indice].update(cliente_editado)
            return jsonify(clientes[indice])
        
@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_clientes(id):
    '''Exclui cliente por parametro'''
    for indice, cliente in enumerate(clientes):
        if cliente.get('id_cliente') == id:
            del clientes[indice]
            
    return jsonify(clientes)
   
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    '''Exibe todos os clientes listados'''
    return jsonify(clientes)  

@app.route('/clientes/<int:id>', methods=['GET'])
def listar_clientes_id(id):
    '''Exibe cliente por parametro'''
    for cliente in clientes:
        if cliente.get('id_cliente') == id:
            return jsonify(cliente)

# ----- LOCAÇÃO DE VEICULOS
@app.route('/locacao', methods=['POST'])
def adicionar_locacao():
    '''Registra uma nova locação'''
    nova_locacao = request.get_json()
    # Pego o ID do cliente para alteração 
    id_cliente = nova_locacao.get('id_cliente')
    id_carro = nova_locacao.get('id_carro')

    # Faço a alteração do Id através do método
    altera_status_cliente(id_cliente, True)
    altera_status_carro(id_carro, True)

    locacoes.append(nova_locacao)

    return jsonify(locacoes)

@app.route('/locacao/<int:id>', methods=['DELETE'])
def excluir_locacao(id):
    '''Registra baixa de uma locação apagando-a do sistema'''
    for indice, locacao in enumerate(locacoes):
        if locacao.get('id') == id:
            id_cliente = locacao.get('id_cliente')
            id_carro = locacao.get('id_carro')
            
            altera_status_cliente(id_cliente, False)
            altera_status_carro(id_carro, False)
            del locacoes[indice]
            
    return jsonify(locacoes)

@app.route('/locacao', methods=['GET'])
def listar_locacoes():
    '''Lista todas as locações em aberto'''
    return jsonify(locacoes)  

@app.route('/locacao/<int:id>', methods=['GET'])
def listar_locacao_id(id):
    '''Exibe locações em aberto por parametro'''
    for locacao in locacoes:
        if locacao.get('id') == id:
            return jsonify(locacao)
 
# ----- Alterações e verificações -----                
def altera_status_cliente(id, status):
    '''Faz alterações no status do cliente'''
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
    '''Faz alterações no status do veiculo'''
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