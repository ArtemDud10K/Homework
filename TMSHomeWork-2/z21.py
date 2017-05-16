list1 = input('Введите первый список\n')
list1 = list1.split()#разделение строки
list2 = input('Введите первый список\n')
list2 = list2.split()#разделение строки
if len(list1) == len(list2):#сравнение списков
	print('Списки равны по длине')
else:
	print('Списки не равны по длине')
