from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from apiPackages.routes import router, get_db
from apiPackages.schemas import apiSchemas
from apiPackages.models import apiModels


@router.get("/users/{username}", response_model=apiSchemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    print(db)
    db_user = read_user_by_name(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

def read_user_by_name(db: Session, username: str):
    #print('get_user_by_username - {}'.format(db.query(models.User).filter(models.User.username == username).first()))
    user_details = db.query(apiModels.User).filter(apiModels.User.username == username).first()
    #print('get_user_by_username - {}'.format(user_details.username))
    return user_details