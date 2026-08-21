from flask import Flask
# 1. Suas importações e configurações iniciais (SQLAlchemy, Blueprints, etc.)

app = Flask(__name__)

# 2. Registro dos seus Blueprints/Rotas existentes
# ex: app.register_blueprint(usuarios_bp)


# 3. Rota Raiz (Adicione aqui para evitar o erro 404 ao acessar a URL base)
@app.route('/')
def home():
    return {"mensagem": "API Connect funcionando com sucesso!"}, 200


# 4. Bloco de execução (SEMPRE no final de tudo)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)