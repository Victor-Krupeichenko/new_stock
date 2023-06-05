from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DECIMAL, Date
from decimal import Decimal
from datetime import date


class Base(DeclarativeBase):
    pass


class Stock(Base):
    __tablename__ = 'stock'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(Date, default=date.today)
    inventary_num: Mapped[int] = mapped_column(nullable=True)
    count: Mapped[int] = mapped_column(nullable=True)
    price: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2), nullable=True)
    status: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return f'Date: {self.date}'
