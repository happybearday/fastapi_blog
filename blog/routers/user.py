from typing import List
from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user as userRepository

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return userRepository.create(request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all(db: Session = Depends(database.get_db)):
    return userRepository.all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(database.get_db)):
    return userRepository.show(id, db)
