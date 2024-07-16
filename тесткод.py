def pas(n):
    password = list()
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                k = str(i) + str(j)
                password.append(k)
    return password


n = int(input('Введите выпавшее число'))
while 3 < n > 20:  
    n = int(input('Введите правильный номер'))

result = str()
a = pas(n)
for i in range(len(a)):
    result += a[i]
print("введите число на след камне", result)
