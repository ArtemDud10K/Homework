data = input('Введите фамилию, имя, возраст, рост и вес\n')
list1 = data.split()
for i in list1:
	if i.isalpha():
		i = str(i)
	else:
		if i.isdigit() and i.find('.') == -1:
			i = int(i)
		else:
			i = float(i)
	print((i, type(i)))
