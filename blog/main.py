from fastapi import FastAPI
from . import Schemas


app = FastAPI()



@app.post('/blog')
def create(request: Schemas.Blog):
    return request