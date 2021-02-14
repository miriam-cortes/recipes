from flask_restx import fields
from recipes.restx import api

category_model = api.model('Category', {
    # 'id': fields.Integer(readonly=True, description='The category unique identifier'),
    'categoryName': fields.String(required=True, description='The category name'),
})

source_model = api.model('Source', {
    # 'id': fields.Integer(readonly=True, description='The source unique identifier'),
    'sourceName': fields.String(required=True, description='The source name')
})

ingredient_model = api.model('Ingredient', {
    # 'id': fields.Integer(readonly=True, description='The ingredient\'s unique identifier'),
    'ingredientName': fields.String(required=True, description='ingredient name'),
    'ingredientQuantity': fields.String(required=True, description='How much?'),
    'ingredientMeasurement': fields.String(required=True, description='cups? Tbsp?'),
    'ingredientPreparation': fields.String(description='any special preparation?')
})

# maybe not needed:
# measurement_units_model = api.model('Measurement units', {
#     'id': fields.Integer(readonly=True, description='The measurement units unique identifier'),
#     'measurement_units_name': fields.String(required=True, description='Measurement units for an ingredient')
# })
# measurement_quantity_model = api.model('Measurement quantity', {
#     'id': fields.Integer(readonly=True, description='The measurement quantity unique identifier'),
#     'measurement_units_quantity': fields.Integer(required=True, description='Measurement units for an ingredient')
# })

recipe_model = api.model('Recipe', {
    # 'id': fields.Integer(readonly=True, description='a recipe'),
    'recipeName': fields.String(required=True, description='a recipe name'),
    'recipeNotes': fields.String(required=False, description='any notes?'),
    'recipeRating': fields.Integer(required=False, description='rating'),
    'recipeInstructions': fields.String(required=True, description='instructions'),
    'ingredients': fields.List(fields.Nested(ingredient_model), required=True),
    'recipeImage': fields.String(required=False, description='source of image from web'),
    'categories': fields.List(fields.Nested(category_model)),
    'source': fields.String(required=True, description='where is this from?')
})

