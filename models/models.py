import enum
from datetime import datetime
from typing import Annotated

from sqlalchemy import Integer, String, DateTime, Float, ForeignKey, Table, Column, Enum
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(DateTime, default=datetime.utcnow, nullable=False)]
updated_at = Annotated[
    datetime, mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
]


association = Table(
    "association",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("categories.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    city_id: Mapped[int] = mapped_column(Integer, ForeignKey("citys.id"), nullable=False)
    prices: Mapped[list["Price"]] = relationship("Price", backref="product", lazy=True)
    features: Mapped[list["Feature"]] = relationship("Feature", backref="product", lazy=True)

    categories: Mapped[list["Category"]] = relationship(
        "Category", secondary=association, back_populates="products", lazy=True
    )


class City(Base):
    __tablename__ = "citys"

    id: Mapped[intpk]
    name_city: Mapped[str] = mapped_column(String(30), nullable=False)

    products: Mapped[list["Product"]] = relationship("Product", backref="city", lazy=True)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name_category: Mapped[str] = mapped_column(String(30), nullable=False)

    products: Mapped[list["Product"]] = relationship(
        "Product", secondary=association, back_populates="categories", lazy=True
    )


class Feature(Base):
    __tablename__ = "features"

    id: Mapped[intpk]
    name_feature: Mapped[str] = mapped_column(String(60), nullable=False)
    value_feature: Mapped[float] = mapped_column(Float, nullable=False)

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)


## import enum
# class PriceType(enum.Enum):
#     RETAIL = "розничная"
#     DISCOUNT = "скидка"
#     WHOLESALE = "оптовая"


## from sqlalchemy import Enum
class PriceType(Enum):
    RETAIL = "розничная"
    DISCOUNT = "скидка"
    WHOLESALE = "оптовая"


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[intpk]
    price: Mapped[float] = mapped_column(Float, nullable=False)

    type_of_price: Mapped[str] = mapped_column(String, nullable=False)
    # type_of_price: Mapped[PriceType]
    # type_of_price: Mapped[PriceType] = mapped_column(Enum(PriceType), nullable=False)

    link_of_the_product: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)


# from db import engine
#
# Base.metadata.create_all(engine)
