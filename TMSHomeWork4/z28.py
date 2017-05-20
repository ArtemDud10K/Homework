def decor(func):
	def transform(l, *args):
		for i in args:
			l.append(i)
		return func(l)
	return transform

def sum_(l):
	summ = 0
	for i in l: 
		summ += i
	print (f'Сумма: {summ}')

sum_ = decor(sum_)
print(sum_([1, 2, 3], 4, 5))
