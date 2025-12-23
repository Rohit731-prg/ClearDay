from app.Database.Model.UserModel import UserModel
from fastapi import HttpException
from app.Config.ConnectDb import collection_user
from app.Utils.hashPassword import compairPassword
from app.Utils.token import generaytToken

async def signUp(user: UserModel) -> dict:
    try:
        await collection_user.insert_one(user.dict())
        return { "message": "User registered successfully" }
    except Exception as e:
        raise HttpException(status_code=400, detail=str(e))
    
async def authentication(email: str, otp: str) -> dict:
    try:
        user = await collection_user.find_one({ "email": email })
        if not user:
            raise HttpException(status_code=400, detail="User not found")
        
        if user["auth"] == True:
            raise HttpException(status_code=400, detail="User already authenticated")
        
        if not user["otp"] == otp:
            raise HttpException(status_code=400, detail="Invalid OTP")
        
        await collection_user.update_one({ "email": email }, { "$set": { "auth": True, "otp": None } })
        return { "message": "User authenticated successfully" }
    except Exception as e:
        raise HttpException(status_code=400, detail=str(e))
    
async def login(email: str, password: str) -> dict:
    try:
        user = await collection_user.find_one({ "email": email })
        if not user:
            raise HttpException(status_code=400, detail="User not found")
        
        if not user["auth"] == True:
            raise HttpException(status_code=400, detail="User not authenticated")
        
        compair = await compairPassword(password, user["password"])
        if not compair:
            raise HttpException(status_code=400, detail="Invalid password")
        
        token = await generaytToken(user)
        return { "token": token, "user": user, "message": "User logged in successfully" }
    except Exception as e:
        raise HttpException(status_code=400, detail=str(e))