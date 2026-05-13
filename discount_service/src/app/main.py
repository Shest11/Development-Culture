from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Discount Service")

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "discount-service"}

@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest):
    # Приоритет: сначала промокод, потом оптовая скидка
    if request.promo_code == "STUDENT10":
        return DiscountResponse(discount_percent=10.0, reason="Student discount (10%)")
    if request.quantity >= 10:
        return DiscountResponse(discount_percent=5.0, reason="Bulk discount (5%)")
    return DiscountResponse(discount_percent=0.0, reason="No discount")