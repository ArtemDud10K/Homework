import string
password = input('Введите пароль\n')
indecators = []
ind = False
for i in password:
	if i in string.ascii_lowercase:
		ind = True
		indecators.append(ind)
	else:
		indecators.append(ind)
	if i in string.ascii_uppercase:
		ind = True
		indecators.append(ind)
	else:
		indecators.append(ind)
	if i in string.digits: 
		ind = True
		indecators.append(ind)
	else:
		indecators.append(ind)
	if i in string.punctuation:
		ind = True
		indecators.append(ind)
	else:
		indecators.append(ind)
print(indecators)
if False in indecators:
	print('Придумайте другой пароль')
else:
	print('Удачный пароль')
