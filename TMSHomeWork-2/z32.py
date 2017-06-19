import math as m
pack_tea = input('Введите кол - во пачек чая(одна пачка - 200 гр)\n')
sugar = input('Введите кол - во пачек сахара(одна пачка - 1 кг)\n')
lemon = input('Введите кол - во лимонов\n')
tea = 1
if pack_tea.isdigit() and sugar.isdigit() and lemon.isdigit():#проверка, что введены числа
	pack_tea = m.trunc(int(pack_tea) * 200 / 20)#расчет кол-во чайников для одного элемента
	sugar = m.trunc(int(sugar) * 1000 / 120)
	lemon = m.trunc(int(lemon) * 2)
	if pack_tea > 0 and sugar > 0 and lemon > 0:
		tea = [pack_tea, sugar, lemon]
		print('Количество чайников', min(tea))
	else:
		print('Вы ввели отрицательное выражение. Такого быть не может')
		exit()
else:
	print('Вы ввели невалидное выражение. Такого быть не может')
	exit()
	 
	  
