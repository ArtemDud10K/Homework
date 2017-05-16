a = int(input('Введите число для извлечения квадратного корня\n'))
x = 1
eps = 0.000001
y = 0
y1 = a ** 1/2
m = 0
while abs(y1 - y) > eps:
	y = (x + a/2)/2
	x += 1
	m += 1 
print(y, m) 
