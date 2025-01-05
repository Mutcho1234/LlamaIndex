"""
This script demonstrates how to use the llama_index library to create a summarization index from a directory of documents and query the index with a summarization query.
"""
from llama_index.core import SummaryIndex, SimpleDirectoryReader

# Define constants
DIR_PATH = r"C:\Users\mutch\source\repos\python-control"

# Load the documents from the directory
documents = SimpleDirectoryReader(DIR_PATH).load_data()

# Create an index from the documents
index = SummaryIndex.from_documents(documents)

# Create a query engine from the index
query_engine = index.as_query_engine(response_mode="tree_summarize")

# Query the engine with a summarization query
response = query_engine.query("<summarization_query>")

# Print the response
print(response)
