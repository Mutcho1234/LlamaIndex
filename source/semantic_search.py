"""
This script demonstrates how to use the Llama Index to perform semantic search on a directory of documents.
"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Define constants
DOCUMENTS_DIRECTORY = r"C:\Users\mutch\source\repos\python-control"

# Load the documents from the directory
documents = SimpleDirectoryReader(DOCUMENTS_DIRECTORY).load_data()

# Create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine from the index
query_engine = index.as_query_engine()

# Get a message from the user
message = input("Enter a message: ")

# Query the engine with the message
response = query_engine.query(message)

# Print the response
print(response)
