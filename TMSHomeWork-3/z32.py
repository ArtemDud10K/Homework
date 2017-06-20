import turtle
import math
print('1. Sin(x)  2.Cos(x)')
ans = int(input('Выберите ответ: '))
if ans == 1:
	x = []
	y = []
	t = turtle.Turtle()
	s = turtle.screensize()
	x_max, y_max = turtle.screensize()
	t.color('red')
	for i in range(math.ceil(y_max)):
		y.append(math.sin(i) * 100)
	for i in range(math.ceil(x_max)):
		x.append(math.sin(math.radians(i)) * 500)
	for i in range(-int(x_max/2), int(x_max/2)):
	#for i in range(-5, 5):
		t.goto(x[i], y[i])
else:
	x = []
	y = []
	t = turtle.Turtle()
	x_max = 500 
	y_max = 400
	t.color('orange')
	for i in range(250):
		y.append(math.cos(i) * y_max / 2)
	for i in range(250):
		x.append(math.cos(math.radians(i)) * x_max / 2)
	for i in range(-int(x_max/2), int(x_max/2)):
		t.goto(x[i], y[i])
turtle.mainloop()
