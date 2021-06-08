##If model table does not exists, it will be crated in the data automatically
import fastapi
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
# from sqlalchemy import engine

from apiPackages.database.database import SessionLocal, engine
from apiPackages.models import apiModels

apiModels.Base.metadata.create_all(bind=engine)

##Golbal parametsrs
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

##API Router
router = fastapi.APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        print('Closed DB connection')
