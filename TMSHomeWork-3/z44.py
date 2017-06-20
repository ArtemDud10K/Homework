row0 = [1, 2, 3]
row1 = [1, 2, 3]
row2 = [1, 2, 3]
matrix = [row0, row1, row2]
new_matrix = []
print(matrix)
for i in range(len(matrix)):
	row = []
	for j in range(len(matrix[i])):
		row.append(matrix[j][i])	
	new_matrix.append(row)
print(new_matrix)
