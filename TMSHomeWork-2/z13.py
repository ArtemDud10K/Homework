import random as r
list1 = input('Введите элеметны списка через пробел\n')
list1 = list1.split()#разделение строки
el = r.choice(list1)#выбор рандомного элемента
print(el)
list2 = input('Введите элеметны списка через пробел\n')
el = int(input('Введите индекс элеметна из списка для вывода рандомом\n'))
list2 = list2.split()
r.shuffle(list2)#перетусовка списка
print(list2[el])
