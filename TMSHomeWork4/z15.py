def depdup(seq):
	res = []
	for i in seq:
		if i not in res:
			res.append(i)
	return res


l = [1, 2, 2, 3, 5, 7, 8, 1, 3]
print(depdup(l))

