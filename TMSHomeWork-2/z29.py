points = []
name1 = input('Введите имя первого игрока\n')
point1 = int(input('Введите количество очков первого игрока\n'))
points.append(point1)
name2 = input('Введите имя второго игрока\n')
point2 = int(input('Введите количество очков второго игрока\n'))
points.append(point2)
name3 = input('Введите имя третьего игрока\n')
point3 = int(input('Введите количество очков третьего игрока\n'))
points.append(point3)
#print(points)
if point1 == max(points):
	print('Поздравляю', name1)
if point2 == max(points):
	print('Поздравляю', name2)
if point3 == max(points):
	print('Поздравляю', name3)
