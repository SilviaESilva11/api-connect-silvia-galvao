from flask import Flask, redirect
from src.models.user_model import User, create_user, db
from src.routes.user_routes import user_router


def create_app(database_uri="sqlite:///:memory:"):
    app = Flask(__name__)

    # Exibe acentos normalmente (sem \u00e3)
    app.json.ensure_ascii = False

    # Configurações do banco e performance
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(user_router, url_prefix="/users")

    @app.route("/")
    def index():
        return redirect("/users/")

    return app


app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.first():
        create_user("Silvia Galvao", "silvia@email.com")

if __name__ == "__main__":
    # debug=False remove o travamento de I/O do PyCharm no Windows
    app.run(debug=False, threaded=True)