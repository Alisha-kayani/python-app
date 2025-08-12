from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router.contact_routes import router as contact_router
from database import connect_database,close_database

app = FastAPI()

app.include_router(contact_router)

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.on_event("startup")    
async def startup():
    await connect_database(app)

@app.on_event("shutdown")
async def shutdown():
    await close_database(app)