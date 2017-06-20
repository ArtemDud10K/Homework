def decor(func):
	def transform(*args):
		l = []
		for i in args:
			if isinstance(i, list):
				for j in  i:
					l.append(j) 
			else:
				l.append(i)
		return func(l)
	return transform

@decor
def sum_(l):
	summ = 0
	for i in l: 
		summ += i
	print (f'Сумма: {summ}')


sum_ = decor(sum_)
print(sum_(1, [2, 3], 4, 5))
