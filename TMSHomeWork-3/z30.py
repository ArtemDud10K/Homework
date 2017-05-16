num = int(input('Введите число для подсчет факториала: '))
faq = 1
for i in range(1, num + 1):
	faq *= i 
print(f'Факториал от числа {num} равен:', faq)
