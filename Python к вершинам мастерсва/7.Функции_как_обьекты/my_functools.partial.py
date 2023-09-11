from processing_of_parameters import tag
from functools import partial

picture = partial(tag, 'img', class_='pic-frame')
#  Мы создаем частичную функцию picture, которая на основе функции tag уже имеет два аргумента:
# 'img': Это первый аргумент, который будет передаваться функции tag. В данном случае, это имя тега HTML - 'img'.
# class_='pic-frame': Это второй аргумент, который будет передаваться функции tag. В данном случае, это атрибут class с значением 'pic-frame'.

print(picture(src='wumpus.jpeg'))