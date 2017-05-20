import random
import time
def action():
	for i in range(random.randint(0,2)):
		time.sleep(random.randint(0, 2))
def mesh(action):
	t1 = time.time()
	res = action	
	t2 = time.time()
	print(t2 - t1)
	return action
print(mesh(action()))
