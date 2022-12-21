from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'modelo': 'Honda Civic',
        'status': 'Alugado'
    },
      {
        'id': 2,
        'modelo': 'Chevrolet Onix',
        'status': 'Disponivel'
    },
          
          
]
# Listando todos os carros
@app.route('/carros')
def listar_carros():
    return jsonify(carros)    

# Executa a aplicação
app.run(port=5000, host='localhost', debug=True)