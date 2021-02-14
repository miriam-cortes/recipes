

##############
#  RECIPES   #
##############
def create_recipe(recipe_name):
    return f"recipe {recipe_name} created"


def delete_recipe(id):
    return f"recipe {id} deleted"


def get_all_recipes():
    return ["recipe 1", "recipe 2", "recipe 3"]


def get_recipe(id):
    return f"recipe {id} gotten"


def update_recipe(id, data):
    return f"recipe {id} updated with {data}"


##############
# CATEGORIES #
##############
def create_category(category_name):
    return f"category {category_name} created"


def delete_category(id):
    return f"category {id} deleted"


def get_all_categories():
    return [
        'breakfast', "lunch", 'dinner',
    ]


def get_category(id):
    return f"category {id} gotten"


def update_category(id, category):
    return f"category {id} updated with this data: {category}"


##############
#  SOURCES   #
##############
def get_all_sources():
    return ["source 1", "source 2", "source 3"]


def get_source(id):
    return f"source {id} gotten"


def update_source(id, data):
    return f"source {id} updated to {data}"


def delete_source(id):
    return f"source {id} deleted"