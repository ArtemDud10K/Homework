import random as r
A = int(input('Введите левую границу промежутка\n'))
B = int(input('Введите правую границу промежутка\n'))
step = int(input('Введите шаг промежутка\n'))
list1 = list(range(A, B, step))
r.shuffle(list1)
el = list1[0]
print('Ваше число:', el)#вывод рандомного числа
