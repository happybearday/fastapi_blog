from typing import List
from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import blog as blogRepository

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepository.create(request, db)


@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepository.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def upgrade(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepository.upgrade(id, request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepository.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepository.show(id, db)
