from fastapi import FastAPI
from database import engine, Base
from app.models.product import Product
from app.routers.products import router as product_router


#Take all the database table blueprints I have defined, connect to PostgreSQL using this engine, and create those tables if they don't already exist.
Base.metadata.create_all(bind=engine)

#Base.metadata-->
#bind=engine -->"Which database should I use to create these tables?"

app = FastAPI()

app.include_router(product_router)

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
