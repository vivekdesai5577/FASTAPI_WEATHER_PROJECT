from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from apiPackages.schemas import apiSchemas
from apiPackages.models import apiModels
from apiPackages.routes import router, get_db

@router.get("/users", response_model=List[apiSchemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(apiModels.User).offset(skip).limit(limit).all()