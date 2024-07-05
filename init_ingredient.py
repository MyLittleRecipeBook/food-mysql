import pandas as pd
import mysql.connector
from mysql.connector import Error
import ast

def connect_to_database(host, database, user, password):
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def get_ingredient_id(connection, ingredient_name):
    """ Get the ingredient_id from the Ingredient table """
    cursor = connection.cursor()
    query = "SELECT ingredient_id FROM Ingredient WHERE ingredient_name = %s"
    cursor.execute(query, (ingredient_name,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def insert_ingredient(connection, ingredient_name):
    """ Insert a new ingredient into the Ingredient table """
    cursor = connection.cursor()
    query = "INSERT INTO Ingredient (ingredient_name) VALUES (%s)"
    cursor.execute(query, (ingredient_name,))
    connection.commit()
    ingredient_id = cursor.lastrowid
    cursor.close()
    return ingredient_id

def ingredient_search_exists(connection, recipe_id, ingredient_id):
    """ Check if the combination of recipe_id and ingredient_id exists in IngredientSearch """
    cursor = connection.cursor()
    query = "SELECT 1 FROM IngredientSearch WHERE recipe_id = %s AND ingredient_id = %s"
    cursor.execute(query, (recipe_id, ingredient_id))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

def insert_ingredient_search(connection, recipe_id, ingredient_id):
    """ Insert a record into the IngredientSearch table """
    cursor = connection.cursor()
    if not ingredient_search_exists(connection, recipe_id, ingredient_id):
        query = "INSERT INTO IngredientSearch (recipe_id, ingredient_id) VALUES (%s, %s)"
        cursor.execute(query, (recipe_id, ingredient_id))
        connection.commit()
    cursor.close()

if __name__ == '__main__':
    # Replace the placeholders with your MySQL server details
    host = '127.0.0.1'
    database = 'mlr-dev-db-tlb'
    user = 'test'
    password = 'test1234'
    csv_file_path = 'data/ingredients.csv'

    connection = connect_to_database(host, database, user, password)
    if connection:
        df = pd.read_csv(csv_file_path)
        df['recipe_ingredient'] = df['recipe_ingredient'].map(lambda x : ast.literal_eval(x))
        for index, row in df.iterrows():
            recipe_id = row['recipe_id']
            print("recipe", recipe_id)
            ingredients = row['recipe_ingredient']
            
            for ingredient in ingredients:
                ingredient_id = get_ingredient_id(connection, ingredient)
                if not ingredient_id:
                    ingredient_id = insert_ingredient(connection, ingredient)
                insert_ingredient_search(connection, recipe_id, ingredient_id)
        
        connection.close()
        print("MySQL connection is closed")
