import time
import asyncio


async def start_strongmen(name, power):
    print(f'Силач {name} начал соревнование!' )
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i + 1} шар!')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task1 = asyncio.create_task(start_strongmen('Pasha', 3))
    task2 = asyncio.create_task(start_strongmen('Denis', 4))
    task3 = asyncio.create_task(start_strongmen('Apollon', 5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())



