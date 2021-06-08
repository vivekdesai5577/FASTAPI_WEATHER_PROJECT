# import fastapi
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from passlib.context import CryptContext
# from sqlalchemy.orm import Session
# #
# from apiPackages.schemas import apiSchemas
# from apiPackages.models import aptModels
# from apiPackages.database.database import engine, SessionLocal
#
# ##If model table does not exists, it will be crated in the data automatically
# aptModels.Base.metadata.create_all(bind=engine)
#
# ##Golbal parametsrs
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
# ##API Router
# router = fastapi.APIRouter()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# # Get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# ###Route for create new user with POST
# ###Input parameters username, email and password
# @router.post("/create_user", response_model=apiSchemas.User)
# def create_new_user(user: apiSchemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         print('Username already registered')
#         raise HTTPException(status_code=400, detail="Username already registered")
#     print('New user request - Create user')
#     return create_user(db=db, user=user)
#
# ##Function to check if user is already exists
# ##Parameters DB session and username
# def get_user_by_username(db: Session, username: str):
#     ##Query the user details from user table
#     user_details: aptModels.User = db.query(aptModels.User).filter(aptModels.User.username == username).first()
#     print('get_user_by_username - {}'.format(user_details.username))
#     return user_details
#
# ##Create new use function - if user is not present on DB then insert new user details to tables.
# def create_user(db: Session, user: apiSchemas.UserCreate):
#     #fake_hashed_password = user.password + "notreallyhashed"
#     db_user = aptModels.User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
# ##Convert plain password to encrytted format
# def get_password_hash(password):
#     print('Plain password - {}, has_passwpord - {}'.format(password, pwd_context.hash(password)))
#     return pwd_context.hash(password)
