row0 = [1, 2, 3]
row1 = [1, 2, 3]
row2 = [1, 2, 3]
matrix = [row0, row1, row2]
new_matrix = []
for i in range(len(matrix)):
	for j in range(len(matrix)):
		new_matrix.append(matrix[j][i])
print(new_matrix)
