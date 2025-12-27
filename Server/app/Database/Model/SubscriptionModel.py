from pydantic import BaseModel, Field, field_validator
from datetime import date
from enum import Enum

class PaymentCycle(str, Enum):
    monthly = "monthly"
    yearly = "yearly"

class Status(str, Enum):
    pending = "pending"
    due = "due"

class SubscriptionModel(BaseModel):
    user: str = Field(..., min_length=1)
    service: str = Field(..., min_length=1)
    cost: float = Field(..., gt=0)
    renewalDate: date = Field(...)
    @field_validator("renewalDate")
    @classmethod
    def check_due_date(cls, v):
        if v < date.today():
            ValueError("Due date cannot be in the past")
        return v

    paymentMethod: str = Field(..., min_length=1)
    paymentCycle: str = "Monthly"
    status: str = "Active"

class UpdateScription(BaseModel):
    cost: float = Field(..., gt=0)
    renewalDate: date = Field(...)
    @field_validator("renewalDate")
    @classmethod
    def check_due_date(cls, v):
        if v < date.today():
            ValueError("Due date cannot be in the past")
        return v
    
    paymentMethod: str = Field(..., min_length=1)
    paymentCycle: str = PaymentCycle.monthly
    status: str = Status.due