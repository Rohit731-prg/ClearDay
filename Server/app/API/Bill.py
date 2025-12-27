from fastapi import APIRouter, HTTPException, Response
from app.Curd.BillCurd import createNewBill, changeStatus, getAllBills
from app.Database.Model.BillModel import BillModel

router = APIRouter(
    prefix="/bill",
    tags=["bill"]
)

@router.post("/newBillCreate")
async def createBillRouter(
    response: Response,
    request: BillModel
) -> dict:
    try:
        res = await createNewBill(request)
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/updateStatus/{id}")
async def updateStatuseRouter(
    response: Response,
    status: str,
    id: str
) -> dict:
    try:
        res = await changeStatus(status, id)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/getAllBills/{id}")
async def getAllBillsRouter(
    response: Response,
    id: str
) -> list:
    try:
        bills = await getAllBills(id)
        response.status_code = 200
        return bills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))