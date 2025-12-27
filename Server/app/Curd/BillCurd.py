from app.Database.Model.BillModel import BillModel
from app.Database.Model.UserModel import UserModel
from app.Config.ConnectDb import collection_user, collection_bill
from fastapi import HTTPException

async def createNewBill(request: BillModel) -> dict:
    try:
        user = await collection_user.find_one({ "userId": request.userId })
        if not user:
            raise HTTPException(status_code=400, detail="User is not valid")
        if not user["auth"] == False:
            raise HTTPException(status_code=400, detail="User is not valid")

        await collection_bill.insert_one(request)
        return { "message": "New bill has created!" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def changeStatus(status: str, id: str) -> dict:
    try:
        bill = await collection_bill.find_one({ "_id": id })
        if not bill:
           raise HTTPException(status_code=400, detail="bill not found")

        await collection_bill.update_one(
            { "_id": id },
            { status: status }
        )
        return { "message": "Bill update successfully! "}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def getAllBills(id: str) -> list:
    try:
        bills = await collection_bill.find({ "userId": id }).to_list()
        return bills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))