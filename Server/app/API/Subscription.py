from app.Curd.SubscriptionCurd import createNewSubscription
from fastapi import APIRouter, HTTPException
from app.Database.Model.SubscriptionModel import SubscriptionModel

route = APIRouter(
    prefix="/subscription",
    tags=["Subscription"]
)

@route.post("/create-new-subscription")
async def createNewSubscriptionRoute(subscription: SubscriptionModel) -> dict:
    try:
        res = await createNewSubscription(subscription)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))