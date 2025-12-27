from pydantic import BaseModel, Field, field_validator
from datetime import date
from enum import Enum

class Frequency(str, Enum):
    monthly = "monthly"
    yearly = "yearly"

class Status(str, Enum):
    pending = "pending"
    paid = "paid"

class BillModel(BaseModel):
    userId: str = Field(..., min_length=1)
    title:  str = Field(..., min_length=1)
    amount:  float = Field(..., gt=0)
    dueDate:  date = Field(...)
    @field_validator("dueDate")
    @classmethod
    def check_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        else:
            return v

    frequency:  str = Frequency.monthly
    status:  str = Status.pending