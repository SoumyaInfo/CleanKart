from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, DateTime
from sqlalchemy.sql import func

from database import Base

  #"I want a database table representing products.(BASE)"
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    description = Column(Text, nullable=True)

    price = Column(Numeric(10, 2), nullable=False)

    discount_price = Column(Numeric(10, 2), nullable=True)

    stock = Column(Integer, nullable=False, default=0)

    image_url = Column(String(500), nullable=True)

    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
        )