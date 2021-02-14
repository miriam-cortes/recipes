#!/usr/bin/python
import psycopg2
from recipes.lib.connect import config


def create_tables():
    commands = (
        # """
        # CREATE TABLE recipes (
        #     recipe_id SERIAL PRIMARY KEY,
        #     recipe_name VARCHAR(200) NOT NULL,
        #     recipe_notes VARCHAR(225),
        #     recipe_rating FLOAT,
        #     recipe_instructions VARCHAR(30000)
        # )
        # """,
        # """ CREATE TABLE measurement_units (
        #     measurement_id SERIAL PRIMARY KEY,
        #     measurement_name VARCHAR(50)
        # )
        # """,
        # """ CREATE TABLE measurement_qty (
        #     measurement_quantity_id SERIAL PRIMARY KEY,
        #     quantity_amount FLOAT NOT NULL
        # )
        # """,
        # """ CREATE TABLE ingredients (
        #     ingredient_id SERIAL PRIMARY KEY,
        #     ingredient_name VARCHAR(50) NOT NULL
        # )
        # """,
        # """ CREATE TABLE sources (
        #     source_id SERIAL PRIMARY KEY,
        #     source_name VARCHAR(255) NOT NULL,
        #     source_url VARCHAR(255)
        # )
        # """,
        # """CREATE TABLE categories (
        #     category_id SERIAL PRIMARY KEY,
        #     category VARCHAR(100)
        # )
        # """,
        # """CREATE TABLE recipe_ingredients (
        #     recipe_id INTEGER NOT NULL,
        #     measurement_id INTEGER NOT NULL,
        #     measurement_quantity_id INTEGER NOT NULL,
        #     ingredient_id INTEGER NOT NULL,
        #     PRIMARY KEY (recipe_id , measurement_id , measurement_quantity_id , ingredient_id),
        #     FOREIGN KEY (recipe_id)
        #         REFERENCES recipes (recipe_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE,
        #     FOREIGN KEY (measurement_id)
        #         REFERENCES measurement_units (measurement_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE,
        #     FOREIGN KEY (measurement_quantity_id)
        #         REFERENCES measurement_qty (measurement_quantity_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE,
        #     FOREIGN KEY (ingredient_id)
        #         REFERENCES ingredients (ingredient_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # )
        # """,
        # """CREATE TABLE recipe_categories (
        #     recipe_id INTEGER NOT NULL,
        #     category_id INTEGER NOT NULL,
        #     PRIMARY KEY (recipe_id , category_id),
        #     FOREIGN KEY (recipe_id)
        #         REFERENCES recipes (recipe_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE,
        #     FOREIGN KEY (category_id)
        #         REFERENCES categories (category_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # )
        # """,
        # """DROP TABLE recipe_types
        # """
        # """CREATE TABLE recipe_sources (
        #     recipe_id INTEGER NOT NULL,
        #     source_id INTEGER NOT NULL,
        #     PRIMARY KEY (recipe_id , source_id),
        #     FOREIGN KEY (recipe_id)
        #         REFERENCES recipes (recipe_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE,
        #     FOREIGN KEY (source_id)
        #         REFERENCES sources (source_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # )
        # """
    )

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # creates a cursor
        cur = conn.cursor()

        # create table one by one
        for command in commands:
            print(f"executing {command}")
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    create_tables()
