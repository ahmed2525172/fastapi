from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import Schemas, models
from database import engine
from database import SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: Schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destory(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == 
                                 id).delete(synchronize_session=False)
    db.commit()
    return 'done'




@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated'


@app.get('/blog/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'The Blog with id {id} is unavailable')
    return blog