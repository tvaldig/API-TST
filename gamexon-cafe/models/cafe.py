from sqlalchemy import Column, String, Integer, Boolean, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config.db import Base

class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=False)
    category = Column(String, nullable=True)
    available = Column(Boolean, default=True)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=datetime.now())
    total_amount = Column(DECIMAL, nullable=False)
    order_details = relationship("OrderDetails", back_populates="order")

class OrderDetails(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=False)

    order = relationship("Order", back_populates="order_details")
    menu = relationship("Menu")

class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    payment_date = Column(DateTime, default=datetime.now())
    amount = Column(DECIMAL, nullable=False)
    status = Column(String, nullable=False)

    order = relationship("Order")
