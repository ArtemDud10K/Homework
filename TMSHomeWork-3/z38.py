data = input('Введите фамилию, имя, возраст, рост и вес\n')
list1 = data.split()
for i in list1:
	surname = str(list1.pop(0))
	name = str(list1.pop(0))
	age = int(list1.pop(0))
	higth = float(list1.pop(0))
	weight = float(list1.pop(0))
print(f'Имя: {name} {type(name)}')   
print(f'Фамилия: {surname} {type(surname)}')
print(f'Возраст: {age} {type(age)}')
print(f'Рост: {higth} {type(higth)}')
print(f'Вес: {weight} {type(weight)}')