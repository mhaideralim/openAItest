from fastapi import FastAPI

from v1.api.router import ask_router
from v1.api.database import connection

app = FastAPI()
app.include_router(ask_router.router)
