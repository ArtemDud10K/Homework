import random as r 
prob = {}
l1 = []
l2 = []
for i in range(10):
	s = 0
	p = r.randint(1, 6)
	l1.append(p)
	if p == 1:
		s += 1
	#prob.fromkeys(l1, s + 1)
print(prob.items())
