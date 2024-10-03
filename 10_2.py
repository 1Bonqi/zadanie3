from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy = self.enemy - self.power
            self.days += 1
            sleep(1)
            print(f'{self.name} сражается {self.days} дней, осталось {self.enemy} войнов')
        print(f'{self.name} одержал победу спустя {self.days} дней')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')