size = int(input('Введите размер списка: '))
list_nuber = []
print('Введите элементы списка')
for i in range(size):
	num = int(input())
	list_nuber.append(num)
print('---------')
for i in range(size):
	print(list_nuber[i])
