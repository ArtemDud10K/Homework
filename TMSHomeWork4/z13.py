def sort_dict(d):
	l = []
	for i in d:
		max1 = max(d)
	if max1 in d:
		return(max1, d.setdefault(max1))
	else:
		return print('не сработало')
#проверка
d = {1:'a', 2:'b', 3:'c'}
print(sort_dict(d))
