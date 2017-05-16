number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
print('Список действий: 1. выход 2.+ 3. - 4. * 5. /')
result = 0
ind = int(input('Выберите действие: '))
if ind == 1:
	exit()
if ind == 2:
	result = number1 + number2
	print(result)
if ind == 3:
	result = number1 - number2
	print(result)
if ind == 4:
	result = number1 * number2		
	print(result)
if ind == 5:
	result = number1 / number2
	print(result)
