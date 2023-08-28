class Gizmo:
    def __init__(self) -> None:
        print(f'Gizmo id: {id(self)}')
# доказатество что переменные этикетки,
#  выполняеться правая часть сначала,
# где создаеться обьект.
x = Gizmo()
# y = Gizmo() 10


charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)

print(id(charles), id(lewis))
lewis['balance'] = 950
print(lewis)
