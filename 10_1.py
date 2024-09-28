from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

write_words(10, 'example10_1.txt')
write_words(30, 'example10_2.txt')
write_words(200, 'example10_3.txt')
write_words(100, 'example10_4.txt')
stop_time = datetime.now()
time_res = stop_time - start_time
print(f'Время = {time_res}')
start_time2 = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example10_5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example10_6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example10_7.txt'))
thr_fourh = Thread(target=write_words, args=(100, 'example10_8.txt'))
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourh.start()
thr_first.join()
thr_second.join()
thr_third.join()
thr_fourh.join()
stop_time2 = datetime.now()
time_res2 = stop_time2 - start_time2
print(f'Время 2 = {time_res2}')
