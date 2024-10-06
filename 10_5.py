import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break
            print(f'Данные из {name}:{all_data}')


files = [f'./file {number}.txt' for number in range(1, 5)]
#s1 = datetime.now()
#for i in files:
    #print(i)
    #read_info(i)
#e1 = datetime.now()
#res1 = e1 - s1
#print(f'Время линейного {res1}')
#Время линейного 0:00:09.821759
if __name__ == '__main__ ':
    s2 = datetime.now()
    with multiprocessing.Pool(processes=4) as m:
        m.map(read_info, files)
    e2 = datetime.now()
    res2 = e2 - s2
    print(f'Время мультипроцессора {res2}')
