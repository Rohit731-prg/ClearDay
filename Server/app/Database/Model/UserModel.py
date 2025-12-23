from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    email: str
    password: str
    auth: bool
    otp: str
    image: str

class LoginModel(BaseModel):
    email: str
    password: str