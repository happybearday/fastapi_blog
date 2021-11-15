from sqlalchemy.orm.session import Session
from .. import schemas, models
from fastapi import status, HTTPException
from .. import schemas, models, hashing


def create(request: schemas.Blog, db: Session):
    new_user = models.User(email=request.email,
                           name=request.name, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def all(db: Session):
    users = db.query(models.User).all()
    return users


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user
