from datetime import datetime
from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from middleware.firebase import get_firebase_user_from_token, check_admin_role
from requests import Session
from external_service.gamexon_rec import get_gameprice_by_id
from external_service.parmeaman import create_new_menu_recommendation
from schema.cafe import MenuCreate, MenuResponse, MenuUpdate, OrderCreate, OrderDetailsCreate, OrderDetailsResponse, OrderResponse, RecommendationRequest
from config.db import SessionLocal
from models.cafe import Menu, Order, OrderDetails, Payment
import midtransclient
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_root():
    return "GAMEXON CLOUD CAFE"

@router.get("/menu/", response_model=List[MenuResponse])
def get_menu_items(db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):
    menu_items = db.query(Menu).all()
    return [{"id": item.id, "item_name": item.item_name, "price": item.price, "description": item.description,
             "category": item.category,
             "available": item.available} for item in menu_items]

# CREATE: Add a new menu item
@router.post("/menu/", response_model=MenuResponse, status_code=status.HTTP_201_CREATED, )
def create_menu_item(menu: MenuCreate, db: Session = Depends(get_db), user: dict = Depends(get_firebase_user_from_token)):
    check_admin_role(user)
    new_item = Menu(**menu.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# READ: Get a menu item by ID
@router.get("/menu/{menu_id}", response_model=MenuResponse)
def get_menu_item(menu_id: int, db: Session = Depends(get_db), user: dict = Depends(get_firebase_user_from_token)):
    menu_item = db.query(Menu).filter(Menu.id == menu_id).first()
    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    return menu_item

# UPDATE: Modify an existing menu item
@router.put("/menu/{menu_id}", response_model=MenuResponse, )
def update_menu_item(menu_id: int, menu: MenuUpdate, db: Session = Depends(get_db), user: dict = Depends(get_firebase_user_from_token)):
    check_admin_role(user)
    menu_item = db.query(Menu).filter(Menu.id == menu_id).first()
    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    menu_item.item_name = menu.item_name or menu_item.item_name
    menu_item.description = menu.description or menu_item.description
    menu_item.price = menu.price or menu_item.price
    menu_item.category = menu.category or menu_item.category
    menu_item.available = menu.available if menu.available is not None else menu_item.available

    db.commit()
    db.refresh(menu_item)
    return menu_item

# DELETE: Remove a menu item by ID
@router.delete("/menu/{menu_id}", status_code=status.HTTP_204_NO_CONTENT, )
def delete_menu_item(menu_id: int, db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):
    check_admin_role(user)
    menu_item = db.query(Menu).filter(Menu.id == menu_id).first()
    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    db.delete(menu_item)
    db.commit()
    return {"message": "Menu item deleted successfully"}

@router.post("/order-details/bulk", response_model=List[OrderDetailsResponse], status_code=status.HTTP_201_CREATED, )
def create_order_details_bulk(
    order_details: OrderDetailsCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_firebase_user_from_token)
):

    order = db.query(Order).filter(Order.id == order_details.order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    new_order_details = [
        OrderDetails(order_id=order_details.order_id, menu_id=menu_id)
        for menu_id in order_details.menu_ids
    ]

    db.add_all(new_order_details)
    db.commit()

    grouped_response = {
        order_details.order_id: [detail.menu_id for detail in new_order_details]
    }

    return [
        OrderDetailsResponse(order_id=order_id, menu_ids=menu_ids)
        for order_id, menu_ids in grouped_response.items()
    ]

@router.get("/order-details/", response_model=List[OrderDetailsResponse], )
def get_all_order_details(db: Session = Depends(get_db), user: dict = Depends(get_firebase_user_from_token)):
    check_admin_role(user)
    db_order_details = db.query(OrderDetails).all()

    grouped_orders = {}
    for detail in db_order_details:
        order_id = detail.order_id
        if order_id not in grouped_orders:
            grouped_orders[order_id] = []
        grouped_orders[order_id].append(detail.menu_id)

    # Return grouped response
    return [
        OrderDetailsResponse(order_id=order_id, menu_ids=menu_ids)
        for order_id, menu_ids in grouped_orders.items()
    ]


@router.get("/order-details/order/{order_id}", response_model=OrderDetailsResponse, )
def get_order_details_by_order(order_id: int, db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):
    db_order_details = db.query(OrderDetails).filter(OrderDetails.order_id == order_id).all()
    if not db_order_details:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    menu_ids = [detail.menu_id for detail in db_order_details]
    return OrderDetailsResponse(order_id=order_id, menu_ids=menu_ids)

#CREATE : Create new order
@router.post("/orders/", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):
    new_order = Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

#READ : See all order
@router.get("/orders/", response_model=List[OrderResponse], )
def get_all_order(db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):
    check_admin_role(user)
    return db.query(Order).all()

#READ : See order by id
@router.get("/orders/{id}", response_model=List[OrderResponse], )
def get_order_by_id(id: int, db: Session = Depends(get_db), user: dict = Depends(get_firebase_user_from_token)):
    return db.query(Order).filter(Order.id == id).all()

@router.post('/recommendation')
def create_menu_recommendation(
    gender: str = Query(..., description="Gender of the user"),
    mood: str = Query(..., description="User's mood"),
    food_type: str = Query(..., description="Preferred food type"),
    drink_type: str = Query(..., description="Preferred drink type"),
    activity_level: str = Query(..., description="User's activity level")
):
    try:
        return create_new_menu_recommendation(
            gender=gender,
            mood=mood,
            food_type=food_type,
            drink_type=drink_type,
            activity_level=activity_level,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#CREATE MIDTRANS TRANSACTION
@router.post("/transactions/")
def create_transaction(order_id: int = Query(...), game_id: int =Query(...), db: Session = Depends(get_db),  user: dict = Depends(get_firebase_user_from_token)):

    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    existing_payment = db.query(Payment).filter(Payment.order_id == order_id).first()
    if existing_payment:
        raise HTTPException(status_code=400, detail="Transaction already exists for this order")

     # Fetch game price
    try:
        call_game_price = get_gameprice_by_id(game_id)
        game_price = call_game_price.get("price_per_day")
        if not game_price:
            raise HTTPException(status_code=404, detail="Game price per day not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch game price: {str(e)}")
    

    # Get discount based on recommendation
    discount = float(order.total_amount) * (float(game_price) / 100000)
    gross_amount = int(float(order.total_amount) + float(game_price) - discount)

    snap = midtransclient.Snap(
        is_production=False,
        server_key=os.getenv("MIDTRANS_SERVER_KEY")
    )

    param = {
        "transaction_details": {
            "order_id": f"order-{order.id}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "gross_amount": gross_amount
        },
    }

    try:
        transaction = snap.create_transaction(param)
        transaction_token = transaction["token"]

        new_payment = Payment(
            order_id=order.id,
            payment_date=datetime.now(),
            amount=gross_amount,
            status="pending" 
        )
        db.add(new_payment)
        db.commit()

        return {
            "transaction_token": transaction_token,
            "message": "Transaction created successfully",
             "transaction_details": {
                "order_id": param["transaction_details"]["order_id"],
                "gross_amount": param["transaction_details"]["gross_amount"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create transaction")
    
