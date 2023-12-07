import random

from sqlalchemy.orm import Session

from db.database import SessionLocal
from models.models import City, Category, Feature, Price, Product, PriceType


def insert_data(db: Session):
    city1 = City(name_city=f"Город {random.randint(1,9)}")
    db.add(city1)
    db.commit()

    category1 = Category(name_category=f"Категория {random.randint(1,9)}")
    db.add(category1)
    db.commit()

    product1 = Product(name=f"Товар {random.randint(1,9)}", city_id=city1.id)
    product1.categories.append(category1)
    db.add(product1)
    db.commit()

    feature1 = Feature(name_feature=f"Характеристика {random.randint(1,9)}", value_feature=10.5, product_id=product1.id)
    db.add(feature1)
    db.commit()

    price1 = Price(
        price=random.randint(1, 999),
        type_of_price=PriceType.RETAIL,
        link_of_the_product=f"ссылка_{random.randint(1,9)}",
        product_id=product1.id,
    )
    db.add(price1)
    db.commit()


if __name__ == "__main__":
    with SessionLocal() as db:
        insert_data(db)
