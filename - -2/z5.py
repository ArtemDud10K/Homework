print('Загадай число от 1 до 5, а я отгадаю его с трёх попыток. Загадал?')
print('Твое число больше 3?')
yes = 'y'
answer = input() #введение ответа пользователя
if answer == yes:#сравнение ответа с заданным
	print('Хорошо. Твое число 5?')
	answer = input()
	if answer == yes:
		print('Твое число - 5')
	else:
		print('Твое число - 4')
else: 
	print('Хорошо. Твое число 3?')
	answer = input()
	if answer == yes:
		print('Твое число - 3')
	else:
		print('Хорошо. Твое число 2?')
		answer = input()
		if answer == yes:
			print('Твое число - 2')
		else:
			print('Твое чило - 1')
