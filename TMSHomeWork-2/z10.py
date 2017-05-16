import datetime
date = input('Введите дату в формате гггг.дд.мм\n')
date1 = datetime.datetime.date(datetime.datetime.strptime(date, '%Y.%d.%m')) #перевод даты в нужный формат
date2 = datetime.timedelta(days=1)#приближение в один день
print(date2 + date1)#ответ задачи
