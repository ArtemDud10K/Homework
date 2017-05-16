number = input('Введите число для перевода\n')
sys = int(input('Введите числом систему для перевода(2,8,16)\n'))
if sys == 2:
	number = int(number)
	print('Ваше число в двоичной системе:', bin(number))#преобразование в нужную систему
if sys == 8:
	number = int(number)
	print('Ваше число в восьмеричной системе:', oct(number))
if sys == 16:
	number = int(number)
	print('Ваше число в шестнадцатиричной системе:', hex(number))
