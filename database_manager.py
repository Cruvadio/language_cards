import sqlite3 as sq
from sqlite3 import Error
from datetime import date

class DataBase:

    def __init__(self, name):
        try:
            self.connection = sq.connect(name)
        except Error as e:
            print(f"Error while connecting database:{e}.")
        else:
            print(f"Database {name} successfully loaded.")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def add_new_language (self, foreign, native):
        query = f"""
        CREATE TABLE IF NOT EXISTS {foreign}_{native}(
            original VARCHAR (255) PRIMARY KEY NOT NULL,
            translate VARCHAR (255) NOT NULL,
            last_update VARCHAR (255),
            is_remembered BOOLEAN DEFAULT (FALSE)
        );
        """
        self._execute_query(query)

    def add_new_word(self, word, translate, foreign, native):
        query = f"""
        INSERT INTO
            {foreign}_{native} (original, translate, last_update, is_remembered)
        VALUES
            (?, ?, (SELECT DATE('now')), FALSE) 
"""
        self._execute_query(query, (word, translate))


    def _execute_query(self, query, args=()):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
            print("Query has executed successfully.")
        except Error as e:
            print(f"Error {e} while executing query '{query}'")

    def return_all_table (self, foreign, native):
        query = f"""SELECT * FROM {foreign}_{native}"""
        return self.cursor.execute(query).fetchall()

    def show_tables (self):
        query = "SELECT name FROM sqlite_master WHERE type = 'table'"
        return self.cursor.execute(query).fetchall()




