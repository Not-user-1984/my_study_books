"""
Пример кода для работы с заказами и скидками.

Этот код включает в себя классы и структуры данных для представления клиентов, товаров, заказов и скидок.

Структуры данных:
- Customer: Представляет клиента и его программу лояльности.
- LineItem: Представляет товары в корзине, включая их название, количество и цену.
- Order: Представляет заказ, включая клиента, корзину товаров и применяемую скидку.
- Promotion: Абстрактный базовый класс для скидок. Содержит обязательный метод `discount`.

Классы скидок:
- FidelityPromo: Скидка на основе программы лояльности клиента. 5% скидка, если клиент имеет лояльность более 1000.
- BulkItemPromo: Скидка на товары в большом количестве. 10% скидка на товары, у которых количество в корзине больше или
равно 20.
- LargeOrderPromo: Скидка на большие заказы. 7% скидка, если в заказе есть 10 или более уникальных товаров.

Использование:

"""
from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional


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


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None

    def total(self) -> Decimal:
        """Вычисляет общую стоимость заказа до применения скидки."""
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def dua(self) -> Decimal:
        """Вычисляет стоимость заказа после применения скидки (если есть)."""
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        """Возвращает строковое представление заказа."""
        return f'<Order total: {self.total():.2f} dua : {self.dua():.2f}'


class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Возвращает скидку в виде положительной суммы в долларах."""
        pass


class FidelityPromo(Promotion):
    """Скидка на основе программы лояльности клиента: 5% скидка для клиентов с лояльностью более 1000."""

    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity > 1000:
            return order.total() * rate
        return Decimal(0)


class BulkItemPromo(Promotion):
    """Скидка на товары в большом количестве: 10% скидка на товары с количеством 20 и более."""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount


class LargeOrderPromo(Promotion):
    """Скидка на большие заказы: 7% скидка для заказов с 10 или более уникальными товарами."""

    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)


if __name__ == '__main__':
    joe = Customer("John Doe", 1100)
    ann = Customer("Anna Ivanova", 900)

    cart1 = [
        LineItem('Banana', 4, Decimal('0.5')),
        LineItem('Apple', 10, Decimal('1.5')),
        LineItem('Orange', 6, Decimal('1.2')),
    ]

    cart2 = [
        LineItem('Banana', 30, Decimal('0.5')),
        LineItem('Apple', 20, Decimal('1.5')),
        LineItem('Orange', 15, Decimal('1.2')),
    ]

    order1 = Order(joe, cart1, FidelityPromo())
    order2 = Order(ann, cart1, FidelityPromo())
    order3 = Order(joe, cart2, BulkItemPromo())
    order4 = Order(joe, cart2, LargeOrderPromo())

    print(order1)
    print(order2)
    print(order3)
    print(order4)
