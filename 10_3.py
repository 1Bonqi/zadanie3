import random
from threading import Thread, Lock
from time import sleep

lock = Lock()


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and lock.locked():
                lock.release()
            rand = random.randint(50, 500)
            self.balance += rand
            print(f'Пополнение на {rand}. Баланс:{self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на: {rand}')
            if rand <= self.balance:
                self.balance = self.balance - rand
                print(f'Снятие {rand}.Баланс:{self.balance}')
                sleep(0.001)
            else:
                print(f'Запрос отклонен, недостаточно средств ')
                lock.acquire()
                sleep(0.001)



bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
