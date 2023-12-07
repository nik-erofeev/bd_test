from pydantic import BaseModel


class ProductPriceResponse(BaseModel):
    product_id: int
    product_name: str
    latest_price: float
