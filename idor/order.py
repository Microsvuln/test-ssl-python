from fastapi import FastAPI, Depends, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Mock authentication dependency
def get_current_user():
    return {"username": "testuser"}  # Simulating authenticated user

# Mock Order model
class Order(BaseModel):
    id: int
    description: str

# Mock order service
class OrderService:
    orders = {
        1: Order(id=1, description="Order 1 details"),
        2: Order(id=2, description="Order 2 details"),
    }

    def get_order_by_id(self, neshanid: int) -> Optional[Order]:
        return self.orders.get(neshanid)

order_service = OrderService()

@app.get("/orders/neshandadan", response_model=Order)
def view_order(neshanid: int, user: dict = Depends(get_current_user)):
    order = order_service.get_order_by_id(neshanid)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
