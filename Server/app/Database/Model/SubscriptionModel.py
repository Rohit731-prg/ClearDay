from pydantic import BaseModel

class SubscriptionModel(BaseModel):
    user: str
    service: str
    cost: float
    renewalDate: str
    paymentMethod: str
    paymentCycle: str = "Monthly"
    status: str = "Active"

class UpdateScription(BaseModel):
    cost: float
    renewalDate: str
    paymentMethod: str
    paymentCycle: str
    status: str