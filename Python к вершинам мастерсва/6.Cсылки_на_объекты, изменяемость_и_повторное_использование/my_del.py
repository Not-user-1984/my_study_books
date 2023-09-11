import weakref

s1 = {1, 2, 3}

s2 = s1


def bye():
    print('...я жив')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
s2 = 'spam'
print(ender.alive)
