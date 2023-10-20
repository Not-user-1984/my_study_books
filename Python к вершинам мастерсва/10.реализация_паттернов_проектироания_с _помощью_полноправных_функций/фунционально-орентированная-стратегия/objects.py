from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Callable, NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        """Вычисляет общую стоимость товара."""
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        """Вычисляет общую стоимость заказа до применения скидки."""
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def dua(self) -> Decimal:
        """Вычисляет стоимость заказа после применения скидки (если есть)."""
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        """Возвращает строковое представление заказа."""
        return f'<Order total: {self.total():.2f} dua : {self.dua():.2f}'