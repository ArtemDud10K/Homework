first_list = [1, 2, 3, 4, [5, 6, 7 , 8]] 
list_second = first_list.pop()
for i in range(len(list_second)):
		first_list.append(list_second[i])
print(first_list)
		

