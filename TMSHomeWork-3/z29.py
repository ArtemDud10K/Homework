num = int(input('Введите границу списка: '))
if num == 0:
	print('невозможно')
else:
	list1 = []
	for i in range(num + 1):
		list1.append(i)
	print('Ваш список: ', list1)
