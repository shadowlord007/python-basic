# dbconnection.py
import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, dbuser, dbpass, dbhost, dbport):
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.dbhost = dbhost
        self.dbport = dbport
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.dbuser,
                password=self.dbpass,
                host=self.dbhost,
                port=self.dbport
            )
            self.cursor = self.conn.cursor()
            print("database connection is establish.")
        except psycopg2.error as error:
            print(f"Error connecting to Database {error}")
            self.conn = None
            self.cursor = None
            
    def execute_query(self, query, params=None):
        """Execute a SQL query."""
        if self.conn is None or self.cursor is None:
            print("No database connection.")
            return
        try:
            self.cursor.execute(query, params)
            print("Query executed successfully.")
            self.conn.commit()
            print("Transaction committed.")
        except psycopg2.Error as error:
            print(f"Error executing query: {error}")


    def fetch_results(self):
        """Fetch all results from the last executed query."""
        if self.cursor:
            return self.cursor.fetchall()
        else:
            print("No results to fetch.")
            return []


    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
            print("Cursor closed.")
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
        self.cursor = None
        self.conn = None

    
    
# db = Database("pythonDB", "postgres", "12345", "localhost", "5432")
# db.connect()
# db.execute_query("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(50));")
# db.execute_query("INSERT INTO test (name) VALUES (%s);", ("Nalice",))
# db.execute_query("SELECT * FROM test;")
# result = db.fetch_results()
# print(result)
# db.close()