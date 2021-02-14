import logging

from flask_restx import Resource
from flask_restx import reqparse

from recipes.restx import api
from recipes.lib.get_recipes import create_category, get_all_categories, get_category, update_category, delete_category

log = logging.getLogger(__name__)

categories_space = api.namespace('category', description='Categories')
category_arguments = reqparse.RequestParser()
category_arguments.add_argument('category_name', location='json', type=str)


@categories_space.route('/')
class MainClass(Resource):

    def get(self):
        """Returns a list of all categories"""
        return {
            "categories": get_all_categories()
        }


@categories_space.route('/<string:category_name>')
@api.response(404, 'Category not found')
class CategoryItem(Resource):

    def get(self, category_name):
        """Returns a list of recipes under a category"""
        return get_category(category_name)

    @api.expect(category_arguments)
    @api.response(204, 'Category successfully updated.')
    def put(self, category_name):
        """Updates a recipes category"""
        # if data is None:
        #     return 400, 'No body provided'
        import pdb; pdb.set_trace()
        return update_category(category_name, self.api.payload.get('category_name'))

    @api.expect(category_arguments)
    @api.response(204, 'Category successfully deleted')
    def delete(self, category_name):
        """Deletes a recipes category"""
        return delete_category(category_name)
