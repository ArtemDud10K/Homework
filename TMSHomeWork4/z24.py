def fib(n):
	a, b = 0, 1
	while a < n:
		yield a
		a, b = b, b + a

#проверка
for i in fib(100):
	print(i)
