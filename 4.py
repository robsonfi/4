from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    dados = request.json
    ano_nascimento = dados.get('ano_nascimento')
    ano_atual = dados.get('ano_atual')
    
    idade_anos = ano_atual - ano_nascimento
    idade_meses = idade_anos * 12
    idade_dias = idade_anos * 365  # Aproximado
    
    return jsonify({
        "idade_anos": idade_anos,
        "idade_meses": idade_meses,
        "idade_dias": idade_dias
    })

if __name__ == '__main__':
    app.run(debug=True)

