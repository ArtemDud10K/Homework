value = 0
for i in range(0, 11):
	print('----------------------')
	for j in range(0, 11):
		value = i * j
		print(f'{i:<2d} * {j:<3d} = {value:<3d}  ')
