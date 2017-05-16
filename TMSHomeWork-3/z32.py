import turtle
import math
print('1. Sin(s)  2.Cos(x)')
ans = input('Выберите ответ: ')
if ans == 1:
	x = []
	y = []
	t = turtle.Turtle()
	x_max = 400 
	y_max = 300
	t.color('red')
	for i in range(250):
		y.append(math.sin(i) * y_max / 2)
	for i in range(250):
		x.append(math.sin(math.radians(i)) * x_max / 2)
	for i in range(-int(x_max/2), int(x_max/2)):
		t.goto(x[i], y[i])
else:
	x = []
	y = []
	t = turtle.Turtle()
	x_max = 400 
	y_max = 300
	t.color('orange')
	for i in range(250):
		y.append(math.cos(i) * y_max / 2)
	for i in range(250):
		x.append(math.cos(math.radians(i)) * x_max / 2)
	for i in range(-int(x_max/2), int(x_max/2)):
		t.goto(x[i], y[i])
