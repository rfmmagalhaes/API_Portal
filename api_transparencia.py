from flask import Flask, jsonify

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Carregando os dados do JSON
import json

with open('Transparencia.json', 'r', encoding='utf-8') as f:
    documentos = json.load(f)

# Endpoint para listar todos os documentos
@app.route('/documentos', methods=['GET'])
def listar_documentos():
    """
    Retorna todos os documentos disponíveis.
    """
    return jsonify(documentos)

# Endpoint para buscar documentos por palavra-chave no nome
@app.route('/documentos/buscar/<string:termo>', methods=['GET'])
def buscar_documentos(termo):
    """
    Busca documentos que contenham o termo no nome.
    """
    resultados = [doc for doc in documentos if termo.lower() in doc['nome'].lower()]
    if resultados:
        return jsonify(resultados)
    return jsonify({"erro": "Nenhum documento encontrado"}), 404

# Endpoint para retornar um documento específico pelo nome exato
@app.route('/documentos/nome/<string:nome>', methods=['GET'])
def documento_por_nome(nome):
    """
    Retorna o documento que tenha exatamente o nome fornecido.
    """
    for doc in documentos:
        if doc['nome'].lower() == nome.lower():
            return jsonify(doc)
    return jsonify({"erro": "Documento não encontrado"}), 404

# Executando a API
if __name__ == '__main__':
    app.run(debug=True)
