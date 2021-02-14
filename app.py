import logging

from flask import Blueprint, Flask

from recipes import settings
from recipes.restx import api
from recipes.routes.categories import categories_space
from recipes.routes.recipes import recipes_space
from recipes.routes.source import sources_space

app = Flask(__name__)
log = logging.getLogger(__name__)

# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(recipes_space)
    api.add_namespace(categories_space)
    api.add_namespace(sources_space)
    flask_app.register_blueprint(blueprint)

    # db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info(f">>>>>> Starting development server at http://{app.config['SERVER_NAME']}/api/")
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    initialize_app(app)
    app.run()
