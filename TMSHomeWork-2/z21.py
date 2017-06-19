list1 = input('Введите первый список\n')
list1 = list1.split()#разделение строки
list1 = set(list1)
list2 = input('Введите первый список\n')
list2 = list2.split()#разделение строки
list2 = set(list2)
if list1 == list2:
	print('Списки равны')
else:
	print('Списки не равны. Разница: ', list1^list2)
