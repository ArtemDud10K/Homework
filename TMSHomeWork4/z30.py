import time
def func():
	print('Hello World!')

def func1():
	time.sleep(2)
	func()

while True:
	func1()

