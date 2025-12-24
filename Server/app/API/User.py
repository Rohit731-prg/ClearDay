from fastapi import APIRouter, Form, Response, HTTPException, UploadFile
from app.Config.ConnectDb import collection_user
from app.Utils.hashPassword import generatehash
import random
from app.Utils.uploadImage import uploadImage
from app.Curd.UserCurd import signUp, authentication, login
from app.Database.Model.UserModel import UserModel

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/signup")
async def signUpRoute(
    response: Response,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    image: UploadFile = Form(...)
) -> dict:
    try:
        is_exist = await collection_user.find_one({"email": email})
        if is_exist:
            raise HTTPException(status_code=400, detail="User already exist")
        
        imageURL = await uploadImage(image)
        hashedPassword = generatehash(password)
        otp = random.randint(1000, 9999)
        newUser = {
            "name": name,
            "email": email,
            "password": hashedPassword,
            "auth": False,
            "otp": otp,
            "image": imageURL["url"]
        }
        res = await signUp(UserModel(**newUser))
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.put("/authentication")
async def authenticationRoute(
    response: Response,
    email: str = Form(...),
    otp: str = Form(...)
) -> dict:
    try:
        res = await authentication(email, otp)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/login")
async def loginRoute(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
) -> dict:
    try:
        res = await login(email, password)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))