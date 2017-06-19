import string
password = input('Введите свой пароль: ')
pos = []
if len(password) < 6:
	print('Не подходит по длине')
	pos.append(False)
else:
	pos.append(True)
if len(password) > 16:
	print('Не подходит по длине')
	pos.append(False)
else:
	pos.append(True)
if set(password).isdisjoint(set(string.ascii_lowercase)):
	print('Нет маленьких букв')
	pos.append(False)
else:
	pos.append(True)
if set(password).isdisjoint(set(string.ascii_uppercase)):
	print('Нет больших букв')
	pos.append(False)
else:
	pos.append(True)
if set(password).isdisjoint(set(string.punctuation)):
	print('Нет специальных символов')
	pos.append(False)
else:
	pos.append(True)
if set(password).isdisjoint(set(string.digits)):
	print('Нет цифр')
	pos.append(False)
else:
	pos.append(True)
if False not in pos:
	print('Хороший пароль')
