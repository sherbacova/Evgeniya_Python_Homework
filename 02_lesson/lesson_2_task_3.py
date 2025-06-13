import math


def square(side):

    return math.ceil(side * side)


side = float(input("Сторона квадрата"))
print(f"Площадь квадрата со стороной {side} равна {square(side)}")

