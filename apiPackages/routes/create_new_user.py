from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from apiPackages.routes import router, get_db
from apiPackages.routes import pwd_context
from apiPackages.schemas import apiSchemas
from apiPackages.models import apiModels

###Route for create new user with POST
###Input parameters username, email and password
@router.post("/create_user/", response_model=apiSchemas.User)
def create_new_user(user: apiSchemas.UserCreate, db: Session = Depends(get_db)):
    print(' user schema- {}'.format(user))
    print(' user name- {}'.format(user.username))
    print('DB session - {}'.format(db))
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        print('Username already registered')
        raise HTTPException(status_code=400, detail="Username already registered")
    print('New user request - Create user')
    return create_user(db=db, user=user)

##Function to check if user is already exists
##Parameters DB session and username
def get_user_by_username(db: Session, username: str):
    ##Query the user details from user table
    #print('get_user_by_username - {}'.format(username))
    user_details = db.query(apiModels.User).filter(apiModels.User.username == username).first()
    #print(user_details)
    #print('get_user_by_username - {}'.format(user_details.username))
    return user_details

##Create new use function - if user is not present on DB then insert new user details to tables.
def create_user(db: Session, user: apiSchemas.UserCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = apiModels.User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

##Convert plain password to encrytted format
def get_password_hash(password):
    print('Plain password - {}, has_passwpord - {}'.format(password, pwd_context.hash(password)))
    return pwd_context.hash(password)
