import logging

from flask_restx import Resource

from recipes.restx import api
from recipes.lib.helpers import get_all_sources, get_source, update_source, delete_source

log = logging.getLogger(__name__)

sources_space = api.namespace('source', description='Sources')


@sources_space.route('/')
class MainClass(Resource):

    def get(self):
        """Returns a list of all sources"""
        return {
            "sources": get_all_sources()
        }


@sources_space.route('/<int:id>')
@api.response(404, 'Source not found')
class SourceItem(Resource):

    def get(self, id):
        """Returns a source with a list of recipes"""
        return get_source(id)

    @api.response(204, 'Category successfully updated')
    def put(self, id, data):
        """Updates a recipes source"""
        update_source(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted')
    def delete(self, id):
        """Deletes a source"""
        return delete_source(id)
