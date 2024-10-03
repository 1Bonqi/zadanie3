from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        exp = randint(3, 10)
        sleep(exp)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        exp = len(self.tables)
        for guest in guests:
            if not exp:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            exp = exp - 1

    def discuss_guests(self):
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest.join()
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        else:
                            table.guest = None
            sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
