from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

def create_document(data):
    result = collection.insert_one(data)
    print(f'Document inserted with id: {result.inserted_id}')

def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

def read_document_by_id(doc_id):
    document = collection.find_one({"_id": ObjectId(doc_id)})
    print(document)

def update_document(doc_id, updated_data):
    result = collection.update_one({"_id": ObjectId(doc_id)}, {"$set": updated_data})
    print(f'Modified count: {result.modified_count}')

def delete_document(doc_id):
    result = collection.delete_one({"_id": ObjectId(doc_id)})
    print(f'Deleted count: {result.deleted_count}')

# Example usage
if __name__ == "__main__":
    create_document({"name": "Alice", "age": 30, "city": "New York"})
    read_documents()
    # Replace with the actual document ID you want to update/delete
    # update_document(<your_document_id>, {"age": 31})
    # delete_document(<your_document_id>)
