def sort_dict(d):
	max_v = max(d.values())
	for i in d:
		if d.get(i) == max_v:
			return (i, max_v)
	

#проверка
d = {'a': 3, 'b': 4}
print(sort_dict(d))
