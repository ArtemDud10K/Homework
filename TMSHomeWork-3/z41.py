import string
password = input('Введите пароль: ')
indecators = []
for i in password:
	if i in string.ascii_lowercase:
		indecators.append(True)
	else:
		print('Нет маленьких букв')
		indecators.append(False)
print(indecators)
