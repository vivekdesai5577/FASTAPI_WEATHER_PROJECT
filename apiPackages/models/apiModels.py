from sqlalchemy import Boolean, Column, Integer, String
##Import base from database
from apiPackages.database.database import Base

##Create User model - This should ne same as table
class User(Base):
    __tablename__ = "users"  ##Tables which will be refered in DB

    id = Column(Integer, primary_key=True, index=True)  ##Table ID is th eprimary and it will be auto increameted.
    username = Column(String, unique=True, index=True) ##Name of use
    email = Column(String, index=True) ## User email id
    hashed_password = Column(String) ## User password which will be stored in encrypted
    is_active = Column(Boolean, default=True) ## Weather user is active or inactive

