import pandas as pd
from pymongo import MongoClient


MONGO_URI = "Mongo Conneciton URI"
DB_NAME = 'mlops'
COLLECTION_NAME = 'insurance'
DATA_PATH = 'Path to Dataset'

def data_to_db():

    # Converting data frame to Dictionary
    df = pd.read_csv(DATA_PATH)
    data = df.to_dict("records")
    client = MongoClient(MONGO_URI)
    
    # Creating a database
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Inserting data to the collection
    collection.insert_many(data)
    print('Data Uploaded Successfully')
