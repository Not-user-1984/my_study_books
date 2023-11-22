import copy

from vector2b import Vector2b

v1 = Vector2b(3.0, 4.0)
x, y = v1
vcopy = copy.copy(v1)
octets = bytes(v1)
vscopy = Vector2b.frombytes(bytes(v1))

if __name__ == '__main__':
    print(v1.x, v1.y)
    print(x, y)
    print(v1)
    print(vcopy == v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2b(0, 0)))
    print(vscopy == v1)
    print(format(v1))
    print(format(v1, '3e'))
    print(format(Vector2b(1, 1), 'p'))
