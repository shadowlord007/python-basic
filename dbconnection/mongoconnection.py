from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri, dbname):
        self.uri = uri
        self.dbname = dbname
        self.client = None
        self.db = None
    
    def connect(self):
        try:
            self.client = MongoClient(self.uri)  # Connect using the URI
            self.db = self.client[self.dbname]   # Access the specific database
            print(f"Connected to MongoDB database: {self.dbname}")
        except Exception as error:
            print(f"Error connecting to MongoDB: {error}")
            self.client = None
            self.db = None
            
    def insert_document(self, collection_name, document):
        """Insert a document into a collection."""
        if self.db is None:
            print("No database connection.")
            return
        try:
            collection = self.db[collection_name]  # Get the collection from the database
            result = collection.insert_one(document)
            print(f"Document inserted with ID: {result.inserted_id}")
        except Exception as error:
            print(f"Error inserting document: {error}")
    
    def find_documents(self, collection_name, query=None):
        """Find documents in a collection."""
        if self.db is None:
            print("No database connection.")
            return
        try:
            collection = self.db[collection_name]
            documents = collection.find(query if query else {})
            return list(documents)
        except Exception as e:
            print(f"Error finding documents: {e}")
            return []

    def update_documents(self, collection_name, query, update):
        """Update documents in a collection."""
        if self.db is None:
            print("No database connection.")
            return
        try:
            collection = self.db[collection_name]
            result = collection.update_many(query, update)
            print(f"Documents matched: {result.matched_count}, modified: {result.modified_count}")
        except Exception as e:
            print(f"Error updating documents: {e}")

    def delete_documents(self, collection_name, query):
        """Delete documents from a collection."""
        if self.db is None:
            print("No database connection.")
            return
        try:
            collection = self.db[collection_name]
            result = collection.delete_many(query)
            print(f"Documents deleted: {result.deleted_count}")
        except Exception as e:
            print(f"Error deleting documents: {e}")

    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
        self.client = None
        self.db = None

    def __str__(self):
        return "MongoDB connection management class."

# Example usage
db = MongoDB("mongodb://localhost:27017", "test")
db.connect()
# db.insert_document('test_collection', {'name': 'Bob', 'age': 25})
db.find_documents('test_collection', {'name': 'Bob'})
db.update_documents('test_collection', {'name': 'Bob'}, {'$set': {'age': 31}})
updated_docs = db.find_documents('test_collection', {'name': 'Bob'})
print(updated_docs)

# Delete documents
db.delete_documents('test_collection', {'name': 'Bob'})

# Close the connection
db.close()
