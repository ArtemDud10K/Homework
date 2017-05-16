import random
list_1 = []
for i in range(random.randint(5, 10)):
	list_1.append(random.randint(0, 100))
print(list_1)
border = int(input('Введите граничное значение: '))
list_2 = []
for i in range(len(list_1)):
	if list_1[i] > border:
		list_2.append(list_1[i])
print(list_2)




