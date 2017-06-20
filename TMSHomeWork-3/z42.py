a = int(input('Введите число для извлечения квадратного корня\n'))
x = 0.1
eps = 0
y1 = a ** 1/2
iteration = 0
y = x * 10
while abs(y1 - y) > eps:
	y = (x + a/2)/2
	x += 0.1
	iteration += 1
print(y, iteration)
