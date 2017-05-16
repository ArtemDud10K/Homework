import turtle
step = int(input('Введите размер шага черепахи: '))
angle = int(input('Введите угол поворота черепахи при рисовке фигуры: '))
ite = int(input('Введите количество повторений: '))
angle1 = int(input('Введите угол поворота черепахи: '))
t = turtle.Turtle()
for i in range(ite + 1):
	for i in range(4):
		t.fd(step)
		t.right(angle) 
	t.right(angle1)

	


