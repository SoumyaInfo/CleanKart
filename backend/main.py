from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Welcome to CleanKart Api"}

@app.get("/api/health")
def health_check():
    try:
        with engine.connect() as connection:
            return{
                "status":"success",
                "message":"CleanKart backend and database are connected"
            }
    except Exception as e:
        return{
            "status":"error",
            "message":"Database connection failed",
            "error": str(e)
        }
