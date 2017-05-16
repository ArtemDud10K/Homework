name1 = input('Введите имя первого игрока\n')
points1 = input('Введите количество очков первого игрока\n')
name2 = input('Введите имя второго игрока\n')
points2 = input('Введите количество очков второго игрока\n')
name3 = input('Введите имя третьего игрока\n')
points3 = input('Введите количество очков третьего игрока\n')
if points1 > points2 and points1 > points3:
	print('Поздравляю', name1)
if points2 > points1 and points2 > points3:
	print('Поздравляю', name2)
if points3 > points1 and points3 > points2:
	print('Поздравляю', name3)
