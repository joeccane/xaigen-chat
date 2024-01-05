import mysql.connector
from mysql.connector import Error

# Database configuration
host = 'localhost'
user = 'your_user'
password = 'your_password'
database = 'your_database_name'

# Connect to MySQL server
try:
    connection = mysql.connector.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=database)
    if connection.is_connected():
        cursor = connection.cursor()
        # SQL query to create a table
        create_table_query = '''CREATE TABLE IF NOT EXISTS tasks (
            task_id VARCHAR(255) PRIMARY KEY,
            task VARCHAR(255) NOT NULL,
            description TEXT,
            context VARCHAR(255),
            info_base TEXT,
            created_date DATE NOT NULL,
            due_date DATE,
            completed BOOLEAN DEFAULT FALSE
        );'''
        cursor.execute(create_table_query)
        connection.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
