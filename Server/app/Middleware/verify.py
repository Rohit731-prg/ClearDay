from fastapi import Request, HTTPException
from jose import jwt
from app.Config.Config import setting
from app.Config.ConnectDb import collection_user

async def verify(request: Request) -> dict:
    try:
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise HTTPException(
                status_code=400,
                detail="Authorization header missing"
            )
        
        scheme, token = auth_header.split(" ")

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=400,
                detail="Invalid authentication scheme"
            )


        
        payload = jwt.decode(token, setting.SERECT_KEY, algorithms=["HS256"])
        data = payload.get("sub")
        user = await collection_user.find_one({ "email": data })
        if not user or not user.get("auth"):
            raise HTTPException(status_code=400, detail="User is not authenticated")

        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 