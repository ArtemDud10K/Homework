size = int(input('Введите размер списка: '))
list_number = []
print('Введите элементы списка')
for i in range(size):
	num = input()
	list_number.append(num)
print(list_number)
print('---------')
for i in list_number:
	print(int(i))
