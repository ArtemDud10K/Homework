import random
import turtle
words = ['mistake', 'notebook', 'glasses']
random.shuffle(words)
s = ''
for i in words:
	s = str(i) 
mist = 0
t = turtle.Turtle()
for i in range(20):
	ans = input('Введите букву: ')
	if ans in s:
		print(ans)
	else:
		mist += 1
		print('нет буквы')
		if mist == 1:
			t.circle(20)
			t.right(90)
		if mist == 2:
			t.fd(50)
			t.right(35)
			t.fd(35)
		if mist == 3:
			t.fd(50)
			t.right(35)
			t.fd(35)
		if mist == 4:
			t.up()
			t.left(180)
			t.fd(35)
			t.right(105)
			t.down()
			t.fd(35)
		if mist == 5:
			t.up()
			t.left(180)
			t.fd(35)
			t.right(40)
		if mist == 6:
			t.fd(30)
			t.right(35)
			t.down()
			t.fd(20)
			t.right(180)
			t.fd(20)
		if mist == 7:
			t.right(105)
			t.fd(20)
			t.right(180)
			t.fd(20)
		if mist == 8:
			t.left(140)
			t.fd(135)
		if mist == 9:
			t.right(90)
			t.fd(135)
		if mist == 10:
			t.right(90)
			t.fd(350)
		if mist == 11:
			t.left(90)
			t.fd(150)
			t.left(180)
			t.fd(300)

