import logging
import traceback

from flask_restplus import Api
import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Politico', description='A voting application')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occured'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {
        'message': 'A database result was required but none was found'
    }, 400
