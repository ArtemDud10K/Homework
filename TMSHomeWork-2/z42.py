from datetime import datetime 
birthday = input('Укажите дату вашего рождения в этом году в формате 2017.дд.мм\n') 
today =  datetime.date(datetime.now())
birthday1 = datetime.date(datetime.strptime(birthday, '%Y.%d.%m'))#преобразование строки в дату
speed = int(input('Введите вашу скорость\n'))
if (birthday1 == today):#сравнение дат
	if speed < 65:#условие для скоростей
		print('Ваш штраф: 0 очков')
	elif 65 <= speed <= 85:
		print('Ваш штраф: 1 очко') 
	else:
		print('Ваш штраф: 2 очка')
else:
	if speed < 60:
		print('Ваш штраф: 0 очков')
	elif 60 <= speed <= 80:
		print('Ваш штраф: 1 очко') 
	else:
		print('Ваш штраф: 2 очка')
