from app.Database.Model.SubscriptionModel import SubscriptionModel
from fastapi import HTTPException
from app.Config.ConnectDb import collection_user, collection_subscription

async def createNewSubscription(subscription: SubscriptionModel) -> dict:
    try:
        user = await collection_user.find_one({ "email": subscription.user })
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        
        await collection_subscription.insert_one(dict(subscription))
        return { "Message": "Subscription created successfully" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def getAllSubscriptions(user: str) -> list:
    try:
        user = await collection_user.findById(user)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        subscriptions = await collection_subscription.find({ user: user }).to_list(length=None)
        if not subscriptions:
            raise HTTPException(status_code=400, detail="No subscriptions found")
        return subscriptions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def updateSubscription() -> dict:
    try:
        
        return { "Message": "Subscription updated successfully" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))