from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool= True, sort: Optional[str] = None):
    #only return the limit bolgs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}



@app.get('/about')
def about():
    return {'data':'about page'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished Blogs'}




@app.get('/blog/{id}')
def show(id: int):
    #Fetch blog with id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}