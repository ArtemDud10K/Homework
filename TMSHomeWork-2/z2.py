number = input('Введите число\n')
if number.isdigit(): #сравение длинны списка
	number = float(number)
	if number % 2 == 0: #сравнение на чётность
		print('Введенное число является чётным')
else:
	print('Условие задачи не соблюдено')
