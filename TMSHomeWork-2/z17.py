d = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
key = int(input('Введите искомый ключ для словаря\n'))
if key in d:# поиск нужного ключа в словаре
	print('Да, такой ключ есть и его значение:', d.get(key, 'пусто'))


