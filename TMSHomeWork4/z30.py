import time
def func():
	time.sleep(2)
	def func1():
		while True:
			time.sleep(2)
			print('Hello!')	
	func1()

func()
