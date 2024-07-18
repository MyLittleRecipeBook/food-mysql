import pandas as pd
import mysql.connector
from mysql.connector import Error
import ast
from collections import defaultdict

def connect_to_database(host, database, user, password):
    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def batch_insert_ingredients(connection, ingredients):
    cursor = connection.cursor()
    query = "INSERT IGNORE INTO Ingredient (ingredient_name) VALUES (%s)"
    cursor.executemany(query, [(ingredient,) for ingredient in ingredients])
    connection.commit()
    cursor.close()

def get_ingredient_ids(connection, ingredients):
    cursor = connection.cursor()
    placeholders = ', '.join(['%s'] * len(ingredients))
    query = f"SELECT ingredient_name, ingredient_id FROM Ingredient WHERE ingredient_name IN ({placeholders})"
    cursor.execute(query, tuple(ingredients))
    result = cursor.fetchall()
    cursor.close()
    return {name: id for name, id in result}

def batch_insert_ingredient_search(connection, ingredient_search_data):
    cursor = connection.cursor()
    query = "INSERT IGNORE INTO IngredientSearch (recipe_id, ingredient_id) VALUES (%s, %s)"
    cursor.executemany(query, ingredient_search_data)
    connection.commit()
    cursor.close()

if __name__ == '__main__':
    host = '127.0.0.1'
    database = 'mlr-dev-db-tlb'
    user = 'test'
    password = 'test1234'
    csv_file_path = 'data/ingredients.csv'

    connection = connect_to_database(host, database, user, password)
    if connection:
        df = pd.read_csv(csv_file_path)
        df['recipe_ingredient'] = df['recipe_ingredient'].apply(ast.literal_eval)

        # Collect all unique ingredients
        all_ingredients = set()
        recipe_ingredients = defaultdict(list)
        for _, row in df.iterrows():
            recipe_id = row['recipe_id']
            ingredients = row['recipe_ingredient']
            all_ingredients.update(ingredients)
            recipe_ingredients[recipe_id].extend(ingredients)

        # Insert all ingredients in batch
        batch_insert_ingredients(connection, all_ingredients)

        # Get all ingredient IDs in one query
        ingredient_id_map = get_ingredient_ids(connection, all_ingredients)

        # Prepare data for IngredientSearch table
        ingredient_search_data = [
            (recipe_id, ingredient_id_map[ingredient])
            for recipe_id, ingredients in recipe_ingredients.items()
            for ingredient in ingredients
        ]

        # Insert all IngredientSearch records in batch
        batch_insert_ingredient_search(connection, ingredient_search_data)

        connection.close()
        print("MySQL connection is closed")




