import logging

from flask_restx import Resource
from flask_restx import reqparse

from recipes.restx import api
from recipes.lib.get_recipes import create_recipe, get_all_recipes, get_recipe, update_recipe, delete_recipe
from recipes.lib.models import recipe_model

log = logging.getLogger(__name__)

recipes_space = api.namespace('recipes', description='Recipes')
recipe_arguments = reqparse.RequestParser()
recipe_arguments.add_argument('recipe_name', location='json', type=int)
recipe_arguments.add_argument('ingredients', location='json')


@recipes_space.route('/')
class MainClass(Resource):

    @api.marshal_list_with(recipe_model)
    def get(self):
        """Returns a list of all recipes"""
        return {
            "recipes": get_all_recipes()
        }

    @api.expect(recipe_model)
    @api.response(201, 'Recipe successfully created.')
    def post(self):
        """Creates a new recipe"""
        create_recipe(self.api.payload.get('recipe_name'))
        return None, 201


@recipes_space.route('/<string:recipe_id>')
@api.response(404, 'Recipe not found')
class RecipeItem(Resource):

    def get(self, recipe_id):
        """Returns a recipe"""
        return get_recipe(recipe_id)

    @api.expect(recipe_arguments)
    def put(self, recipe_id, data):
        """Updates a recipes"""
        return update_recipe(recipe_id, data)

    @api.response(204, 'Recipe successfully deleted')
    def delete(self, recipe_id):
        """Deletes a recipe"""
        return delete_recipe(recipe_id)
