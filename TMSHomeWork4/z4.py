def all_(l):
	l1 = []
	if len(l) == 0:
		return True
	for i in l:
		if i != False:
			l1.append(i)
		else:
			return False
	return True
		
#проверка
print(all([1, 2, 3]))
print(all_([1, 2, 3]))			
