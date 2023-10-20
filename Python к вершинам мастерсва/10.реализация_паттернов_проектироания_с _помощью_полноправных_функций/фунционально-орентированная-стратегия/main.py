from decimal import Decimal
from best_promo import best_promo
import objects
import promo


def test_func_strategy():
    joe = objects.Customer("John Doe", 1100)
    ann = objects.Customer("Anna Ivanova", 900)

    cart1 = [
        objects.LineItem('Banana', 4, Decimal('0.5')),
        objects.LineItem('Apple', 10, Decimal('1.5')),
        objects.LineItem('Orange', 6, Decimal('1.2')),
    ]

    cart2 = [
        objects.LineItem('Banana', 30, Decimal('0.5')),
        objects.LineItem('Apple', 20, Decimal('1.5')),
        objects.LineItem('Orange', 15, Decimal('1.2')),
    ]

    order1 = objects.Order(joe, cart1, promo.fidelity_promo)
    order2 = objects.Order(ann, cart1, promo.fidelity_promo)
    order3 = objects.Order(joe, cart2, promo.bulk_item_promo)
    order4 = objects.Order(joe, cart2, promo.large_order_promo)

    print(order1)
    print(order2)
    print(order3)
    print(order4)

    print("Best promo for order1:", best_promo(order1))
    print("Best promo for order2:", best_promo(order2))
    print("Best promo for order3:", best_promo(order3))
    print("Best promo for order4:", best_promo(order4))

if __name__ == '__main__':
    test_func_strategy()
