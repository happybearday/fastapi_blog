from fastapi import APIRouter
from fastapi import Depends
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash
from datetime import timedelta

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    # generate a jwt token and return
    print(user)
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
