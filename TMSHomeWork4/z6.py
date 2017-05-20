def enumerate_ (seq):
	idx = 0
	for i in seq:
		print(i)
		i += 1
	
l = [1, 2, 3]
for idx, item in enumerate(l):
        print(idx)

for idx, item in enumerate_(l):
        print(idx)
