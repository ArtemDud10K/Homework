import random
def min_(l):
	min1 = l[0]
	for i in l:
		if i < min1:
			min1 = i
	return min1
	
# проверка
l = []
for i in range(random.randint(5, 10)):
	l.append(random.randint(0, 10))
print(l)
print(min_(l))
			 
