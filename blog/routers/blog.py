from typing import List
from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(
        title=request.title, body=request.body, published_at=request.published_at, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/blog/{id}', tags=["blogs"])
def destroy(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def upgrade(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    data = jsonable_encoder(request)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")
    blog.update(data)
    db.commit()
    return "updated"


@router.get("/blog", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=["blogs"])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
def show(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")
    return blog
