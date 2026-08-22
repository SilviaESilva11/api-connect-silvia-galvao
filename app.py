from flask import Flask


def create_app():
  app = Flask(__name__)

  # Suas rotas, blueprints e extensões entram aqui
  @app.route("/")
  def home():
    return {"mensagem": "API Connect funcionando com sucesso!"}

  return app


if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)