import logging

from flask import request
from flask_restplus import Resource
from ..restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('office', description='Operations related to office')


@ns.route('/')
class Office(Resource):
    """Welcome page for the app"""
    @ns.doc('welcome_page')
    def get(self):
        return 'welcome to Politico', 200
