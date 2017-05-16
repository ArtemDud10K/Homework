import turtle

first = 30
second = first*2
n_angle = 7
step = 50
t = turtle.Turtle()
t.speed(150)
while True:
	t.clear()
	t.penup()
	t.goto(0, 0)
	t.right(t.heading())
	t.pendown()
	for i in range(n_angle):
		t.forward(step)
		t.left(first)
		t.forward(step)
		t.right(second)
	if abs(t.pos()) < 1:
		break
	first += 1
	second = first*2

print(first)
print(second)
