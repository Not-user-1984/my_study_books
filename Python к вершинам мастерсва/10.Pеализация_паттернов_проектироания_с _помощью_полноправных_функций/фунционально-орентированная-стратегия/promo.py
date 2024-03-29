from decimal import Decimal

from best_promo import promotion
from objects import Order


@promotion
def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity > 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item_promo(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order_promo(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
