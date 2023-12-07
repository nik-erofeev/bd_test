from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from crud.crud import get_products_with_latest_price
from db.database import get_db

router = APIRouter(tags=["Test"])


@router.get("/", summary="получение товаров", description="получение товаров с новой ценой", response_model=list[dict])
async def read_product(db: Session = Depends(get_db)):
    result = get_products_with_latest_price(db)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products")

    response_data = []
    for product, price in result:
        response_data.append({"product_id": product.id, "product_name": product.name, "latest_price": price.price})

    return response_data
