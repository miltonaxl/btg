import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

print(" mongo_uri ", mongo_uri)
database_name = os.getenv("MONGO_DB", "default_database")  # Provide a default value if not set

client = MongoClient(mongo_uri)

def seed_run():
    """ Seed the funds collection with initial data. """
    
    list_funds = [
        {"name": "FPV_BTG_PACTUAL_RECAUDADORA", "category": "FPV", "minimum_amount": 75000},
        {"name": "FPV_BTG_PACTUAL_ECOPETROL", "category": "FPV", "minimum_amount": 125000},
        {"name": "DEUDAPRIVADA", "category": "FIC", "minimum_amount": 50000},
        {"name": "FDO-ACCIONES", "category": "FIC", "minimum_amount": 250000},
        {"name": "FPV_BTG_PACTUAL_DINAMICA", "category": "FPV", "minimum_amount": 100000},
    ]
    
    # Access the database explicitly using the database name
    db = client[database_name]
    
    print(database_name)
    funds_collection = db.funds
    
    # Check if the collection already contains data
    if funds_collection.count_documents({}) > 0:
        print("Funds data already seeded.")
        return
    
    # Insert the data into the collection
    funds_collection.insert_many(list_funds)
    print("Funds data seeded successfully.")

# Run the seeder
seed_run()
