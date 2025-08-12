from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase
from dotenv import load_dotenv
import os 
from typing import AsyncGenerator
from fastapi import FastAPI,Request

load_dotenv()

MONOGO_URL = os.getenv("MONGO_URL")
print(MONOGO_URL)
DATABASE_NAME ="my_database_python"

async def connect_database(app:FastAPI):

    try:
        client =AsyncIOMotorClient(MONOGO_URL)
        db = client[DATABASE_NAME]

        await client.admin.command('ping')

        app.state.mongodb_client = client
        app.state.database = db

        print("Connected to MongoDB")

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

async def close_database(app:FastAPI):

    if hasattr(app.state,'mongodb_client'):
        app.state.mongodb_client.close()
        print("Database disconnected successfully")

# async def get_db(request:Request)->AsyncGenerator[AsyncIOMotorClient,None]: 
async def get_db(request:Request)->AsyncGenerator[AsyncIOMotorDatabase,None]:
    database = request.app.state.database # <-- Corrected line
    try:
        yield database
    finally:
        pass

async def get_contacts_collection(request:Request)->AsyncGenerator:
    collection = request.app.state.database["contacts"] # <-- Corrected line
    try:
        yield collection
    finally:
        pass