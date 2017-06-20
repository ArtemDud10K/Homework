import random
import time
n = 0
def decor(func):
	def mesh(*args):
		global n 
		t1 = time.time()
		n += 1 
		print(f'Количесвто запусков {n}')
		t2 = time.time()
		print('Время работы', t2 - t1)
	return mesh

@decor
def func(*args):
	return args


func = decor(func)
print(func(1, 2, ['c', 'd', 'e']))
