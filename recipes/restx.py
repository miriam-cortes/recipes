import logging
import traceback

from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

from recipes import settings

log = logging.getLogger(__name__)

api = Api(
    version='0.1',
    title='Miriam & Steve\'s recipes api'
)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {
               'message': 'A database result was required but none was found'
           }, 404
