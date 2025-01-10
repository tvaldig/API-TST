from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MenuBase(BaseModel):
    item_name: str
    description: Optional[str]
    price: float
    category: Optional[str] = None
    available: Optional[bool] = True


class MenuResponse(BaseModel):
    id: int
    item_name: str
    description: Optional[str]
    price: float
    category: Optional[str]
    available: bool

    class Config:
        orm_mode = True

class MenuCreate(BaseModel):
    item_name: str
    description: Optional[str]
    price: float
    category: Optional[str]
    available: Optional[bool] = True

class MenuUpdate(BaseModel):
    item_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    available: Optional[bool] = None


class OrderBase(BaseModel):
    total_amount: float


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    order_date: datetime
    class Config:
        orm_mode = True

class OrderDetailsBase(BaseModel):
    order_id: int
    menu_ids: List[int]


class OrderDetailsCreate(OrderDetailsBase):
    menu_ids: List[int]

class OrderDetailsResponse(OrderDetailsBase):
    menu_ids: List[int]

    class Config:
        orm_mode = True


class PaymentBase(BaseModel):
    order_id: int
    amount: float
    status: str

class PaymentResponse(PaymentBase):
    id: int
    payment_date: datetime
    class Config:
        orm_mode = True

class RecommendationRequest(BaseModel):
    gender: str
    mood: str
    food_type: str
    drink_type: str
    activity_level: str