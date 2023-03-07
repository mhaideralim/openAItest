from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from v1.api.database import model
from v1.api.database.settings import MongoDBSettings, origins
from v1.api.database.model import User, Input, Response

app = FastAPI()

# Set up CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = AsyncIOMotorClient(MongoDBSettings.database_url)
database = client[MongoDBSettings.database_name]


async def init_models():
    await init_beanie(
        database=database,
        document_models=(
           Input,
            # add additional models here
        ),
    )


@app.on_event("startup")
async def on_startup():
    await init_models()
    print("Initializing App")


@app.on_event("shutdown")
async def on_shutdown():
    client.close()
    print("DataBase Connection Failed")
