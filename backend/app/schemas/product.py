#Pydantic schema = how the data should look when it enters/leaves our API.
from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import datetime 


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    discount_price: Optional[Decimal] = None
    stock: int
    image_url: Optional[str] = None
    is_active: bool = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    discount_price: Optional[Decimal] = None
    stock: Optional[int] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    discount_price: Optional[Decimal] = None
    stock: int
    image_url: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

#This will let FastAPI/Pydantic convert a SQLAlchemy Product object into our ProductResponse.
    model_config = ConfigDict(from_attributes=True)