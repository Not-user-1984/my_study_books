from decimal import Decimal
from typing import Callable, List

from objects import Order

Promotion = Callable[[Order], Decimal]

promos: List[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)


def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)
