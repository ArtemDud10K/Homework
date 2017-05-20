def reverse_ (l):
	l1 = []
	for i in l[::-1]:
		l1.append(i)
	return l1
	

print(reverse_([1, 2, 3]))
