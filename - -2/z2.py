number = list(input('Введите число\n'))
if len(number) == 1: #сравение длинны списка
	number = float(number[0])
	if number % 2 == 0: #сравнение на чётность
		print('Введенное число является чётным')
else:
	print('Условие задачи не соблюдено')
