a = 0
b = 1
n = 50
print(a, b, end=' ')
for i in range(2, n + 1):
	c = a + b
	a, b = b, c
	if c < 50:
		print(c, end=' ')
