first_list = [1, 2, [5, 6, 7 , 8], 3, 4] 
for i in first_list:
	if isinstance(i, list):
		second_list = i
		index = first_list.index(second_list)
first_list.pop(index)
first_list.extend(second_list)
print(first_list)		

