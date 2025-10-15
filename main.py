from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blogs'}

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
def comments(id):
    return {'data': {'1', '2'}}