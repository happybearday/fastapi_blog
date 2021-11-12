from typing import List
from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, hashing

router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["users"])
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(email=request.email,
                           name=request.name, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/user", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser], tags=["users"])
def all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/user/{id}", status_code=200, response_model=schemas.ShowUser, tags=["users"])
def show_users(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user
