import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.SFPL_DB
collection = db.sfpl_db

# Fetch data and convert to a list of dictionaries
data = [doc for doc in collection.find()]

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)