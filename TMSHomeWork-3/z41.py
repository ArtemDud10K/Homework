import string
password = input('Введите пароль: ')
indecators_low = []
indecators_up = []
indecators_punc = []
indecators_dig = []
length = 0
for i in password:
	length += 1
	if i in string.ascii_lowercase:
		indecators_low.append(True)
for i in password:
	if i in string.ascii_uppercase:
		indecators_up.append(True)
for i in password:
	if i in string.punctuation:
		indecators_punc.append(True)
for i in password:
	if i in string.digits:
		indecators_dig.append(True)		
if len(indecators_low) == 0:
	print('нет маленьких букв')
if len(indecators_up) == 0:
	print('нет больших букв')
if len(indecators_punc) == 0:
	print('нет специальных символов')
if len(indecators_dig) == 0:
	print('нет чисел')
if length <= 6:
	print('слишком короткий пароль')





















#if length < 6:
#	print('Маленький пароль')	

