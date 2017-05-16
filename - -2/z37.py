from datetime import datetime 
date = input('Укажите дату в формате гггг.дд.мм\n')
date1 = datetime.date(datetime.strptime(date, '%d.%B.%Y'))#преобразование строки
print(date1)
