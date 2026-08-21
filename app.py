# app.py
from flask import Flask
from src.routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)