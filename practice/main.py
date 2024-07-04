from dbconnection import Database

db = Database("pythonDB", "postgres", "12345", "localhost", "5432")
db.connect()
db.execute_query("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(50));")
db.execute_query("INSERT INTO test (name) VALUES (%s);", ("Nalice",))
db.execute_query("SELECT * FROM test;")
result = db.fetch_results()
print(result)
db.close()