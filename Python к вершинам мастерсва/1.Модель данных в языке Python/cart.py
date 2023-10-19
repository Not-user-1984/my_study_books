"""
>>> len(deck)
52


"""
import collections


Cart = collections.namedtuple('Cart', ['rank', 'suit'])


class FrechDeck:
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Cart(rank, suit)for suit in self.suits
                       for rank in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    '?;.0990-999999'


deck = FrechDeck()


print(
    *[_ for _ in deck ][:3],sep="\n"
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
