from typing import List, Optional
from pydantic import BaseModel

###Create user schema which will use by other classes to derive it
class UserBase(BaseModel):
    username: str
    email: str

##For Password - This is same as below
##Classs UserCreate():
##      username: str  ## Userbname and password will be derived from UserBase
##      email: str
##      password: str
class UserCreate(UserBase):
    password: str

##Model equal to table- This is same as below
##Classs User():
##      id: int
##      is_active: bool
##      username: str  ## Userbname and password will be derived from UserBase
##      email: str
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

###Create Token schema which will use by other classes to derive it
class Token(BaseModel):
    access_token: str
    token_type: str

##User token data - same as below
##  class TokenData(BaseModel):
##      access_token: str
##      token_type: str
##      username: Optional[str] = None
class TokenData(BaseModel):
    username: Optional[str] = None

##User UserInDB - same as below
##Classs UserInDB():
##      id: int
##      is_active: bool
##      username: str  ## Userbname and password will be derived from UserBase
##      email: str
##      hashed_password: str
class UserInDB(User):
    hashed_password: str

class Location(BaseModel):
    city: str
    country: str = 'IN'

class weather(Location):
    #{'temp': 303.2, 'feels_like': 304.94, 'temp_min': 303.2, 'temp_max': 308.32, 'pressure': 1001, 'humidity': 54}
    temp_metric: str = 'Celsius'
    temp: Optional[float] = None
    temp_min: Optional[float] = None
    temp_max: Optional[float] = None
    humidity: Optional[float] = None

