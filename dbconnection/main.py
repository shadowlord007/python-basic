from dbconnection import Database

db = Database("pythonDB", "postgres", "12345", "localhost", "5432")
db.connect()

create_table = """
    CREATE TABLE IF NOT EXISTS test (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        created_at TIMESTAMP default CURRENT_TIMESTAMP,
        updated_at TIMESTAMP default CURRENT_TIMESTAMP
    );
"""

insert_value = """
    INSERT INTO test (name) VALUES (%s)
"""

select_table = """
    SELECT * FROM test
"""
delete_value ="""
    DELETE FROM test
    WHERE id=%s
"""

db.execute_query(create_table)
db.execute_query(insert_value, ("Awais",))
db.execute_query(delete_value, ("2"))
db.execute_query(select_table)
result = db.fetch_results()
print(result)
db.close()