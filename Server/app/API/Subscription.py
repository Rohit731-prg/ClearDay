from app.Curd.SubscriptionCurd import createNewSubscription
from fastapi import APIRouter, HTTPException, Response
from app.Database.Model.SubscriptionModel import SubscriptionModel

route = APIRouter(
    prefix="/subscription",
    tags=["Subscription"]
)

@route.post("/create-new-subscription")
async def createNewSubscriptionRoute(response: Response, subscription: SubscriptionModel) -> dict:
    try:
        res = await createNewSubscription(subscription)
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))