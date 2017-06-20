print('Загадай число от 1 до 5. Твое число больше трех?')
ans = input('Ответы только Y/N: ')
if ans == 'y':
	print('Хорошо. Твое число 4?')
	ans = input()
	if ans == 'y':
		print('Твое число 4')
	else:
		print('Твое число 5')
else:
	print('Твое число 3?')
	ans = input()
	if ans == 'y':
		print('Твое число 3')
	else:
		print('Твое число 2?')
		ans = input()
		if ans == 'y':
			print('Твое число 2')
		else:
			print('Твое число 1')
