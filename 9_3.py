first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_res = (len(x) - len(y) for x, y in zip(first, second) if not len(x) == len(y))
second_res = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(first_res))
print(list(second_res))
