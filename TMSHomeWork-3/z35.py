border = int(input('Введите границу суммы квадратов: '))
sum1 = 0
for i in range(border + 1):
	sum1 += i ** 2
	print(f'Сумма на {i:<d} - той итеррации: ', sum1) 
