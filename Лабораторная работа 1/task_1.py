# TODO Написать 3 класса с документацией и аннотацией типов
import math
from typing import Union


class Point:
    """
    >>> point = Point(1,2)
    >>> point2 = point.symmetrical_about_origin()
    >>> print(point2.x, point2.y)
    -1 -2
    >>> point.distance_to(point2)
    4.47213595499958
    """

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = None
        self.init_x(x)

        self.y = None
        self.init_y(y)

    def init_x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError
        self.x = x

    def init_y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError
        self.y = y

    # возвращает объект точки, симметричной данной, относительно начала координат
    def symmetrical_about_origin(self) -> __init__:
        return Point(-self.x, -self.y)

    # возвращает расстояние между данной точкой и подаваемой в метод
    def distance_to(self, p2: __init__):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Door:
    """
    >>> door = Door(100,200)
    >>> print(door.is_open)
    False
    >>> door.open()
    >>> print(door.is_open)
    True
    >>> door.close()
    >>> print(door.is_open)
    False
    """
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        self.width = None
        self.init_width(width)

        self.height = None
        self.init_height(height)

        self.is_open = False

    def init_width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError
        self.width = width

    def init_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError
        self.height = height

    # открывает дверь
    def open(self):
        self.is_open = True

    # закрывает дверь
    def close(self):
        self.is_open = False


class Human:
    """
    >>> h = Human("masha", 19)
    >>> h.say_name()
    masha
    >>> h.age
    19
    >>> h.grow_up()
    >>> h.age
    20
    """
    def __init__(self, name: str, age: int):
        self.name = None
        self.init_name(name)

        self.age = None
        self.init_age(age)

    def init_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_age(self, age):
        if not isinstance(age, int):
            raise TypeError
        if age < 0:
            raise ValueError
        self.age = age

    # увеличивает возраст человека на один
    def grow_up(self):
        self.age += 1

    # пишет в консоль имя человека
    def say_name(self):
        print(self.name)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
