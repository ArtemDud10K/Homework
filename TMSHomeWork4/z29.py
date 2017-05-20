def filter(seq, cond):
	res = []
	for el in seq:
		r = cond(el)
		if r:
			res.append(el)
	return res
	
#проверка
l = [1, 'a', 'b', 2, 3]
