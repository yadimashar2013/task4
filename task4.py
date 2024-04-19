from random import randint


class Buiding:  # Создайте новый класс Buiding с атрибутом total
    total = 0

    def __int__(self):  # инициализатор для класса Buiding
        Buiding.total += 1  # увеличиваем атрибут количества созданных объектов класса Building total


buiding = []
buiding_size = randint(0, 40)
for i in range(40):
    my_buiding = Buiding()
    buiding.append(my_buiding)
    print(buiding_size)