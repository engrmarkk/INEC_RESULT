from extensions import db, migrate
from models import AnnPuResult, \
    Lga, PollingUnit, State, Ward, AnnLgaResult, \
    AgentName, Party, AnnStateResult, AnnWardResult
from flask import Flask
import os
from views import main as main_blueprint


def create_app():
    app = Flask(__name__)
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'inec.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mysecretkey'

    db.init_app(app)
    migrate.init_app(app, db)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'AnnLgaResult': AnnLgaResult,
            'AnnPuResult': AnnPuResult,
            'Lga': Lga,
            'PollingUnit': PollingUnit,
            'State': State,
            'Ward': Ward,
            'AgentName': AgentName,
            'Party': Party,
            'AnnStateResult': AnnStateResult,
            'AnnWardResult': AnnWardResult
        }

    app.register_blueprint(main_blueprint)

    return app
