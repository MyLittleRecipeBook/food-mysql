import mysql.connector
from mysql.connector import Error
import csv

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

def insert_data_from_csv(connection, csv_file_path, table_name):
    """ Insert data from CSV file into MySQL table """
    cursor = connection.cursor()
    try:
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row
            for row in csv_reader:
                # Construct SQL statement with proper quoting and column names
                sql = f"""INSERT INTO {table_name} (recipe_id, recipe_title, recipe_thumbnail, situ_no, cate_no)
                          VALUES (%s, %s, %s, %s, %s)"""
                values = (row[0], row[1], row[2], row[3], row[4])
                print(f"recipe no. {row[0]} inserted")
                cursor.execute(sql, values)  # Execute the SQL statement
            connection.commit()
            print(f"Data from {csv_file_path} has been inserted into the {table_name} table.")
    except Error as e:
        print(f"Error while inserting data into MySQL table: {e}")
    finally:
        cursor.close()

if __name__ == '__main__':
    # Replace the placeholders with your MySQL server details
    host = '127.0.0.1'
    database = 'mlr-dev-db-tlb'
    user = 'test'
    password = 'test1234'
    csv_file_path = 'data/recipes_metadata.csv'
    table_name = 'Recipe'

    connection = connect_to_database(host, database, user, password)
    if connection:
        insert_data_from_csv(connection, csv_file_path, table_name)
        connection.close()
        print("MySQL connection is closed")
