from fastapi import FastAPI
from .database import engine
from .models import user, recipe, comment
from .routers import auth

user.Base.metadata.create_all(bind=engine)
recipe.Base.metadata.create_all(bind=engine)
comment.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Recipe API!"}