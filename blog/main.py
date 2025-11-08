from fastapi import FastAPI
from . import Schemas, models
from database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()



@app.post('/blog')
def create(request: Schemas.Blog):
    return request