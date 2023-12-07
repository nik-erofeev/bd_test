from sqlalchemy import func, and_
from sqlalchemy.orm import Session

from models.models import Price, Product


def get_products_with_latest_price(db: Session):
    subquery = (
        db.query(Price.product_id, func.max(Price.created_at).label("max_created_at"))
        .group_by(Price.product_id)
        .subquery()
    )

    result = (
        db.query(Product, Price)
        .join(subquery, Product.id == subquery.c.product_id)
        .join(Price, and_(Product.id == Price.product_id, Price.created_at == subquery.c.max_created_at))
        .all()
    )

    return result
