T1 = 'Мастера кода'
T2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2


print('В команде %s участников %s' % (T1, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда {title} решила задач: {postfix} '.format(title=T2, postfix=score_2))
print('{} решили задачи за {}с'.format(T2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Сеголня было решено задач {tasks_total}, в среднем по {time_avg} секунды на задачу')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
     print(f'Победа команды {T1}')

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
   print(f'Победа команды {T2}')
else:
    print('Ничья!')