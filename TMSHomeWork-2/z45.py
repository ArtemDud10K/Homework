import time
import difflib
a = 'Введите текст, который вы видете на экране своего компьютера'
print(a)
t1 = time.time()
b = input()
t2 = time.time()
res = round(difflib.SequenceMatcher(a = a, b = b).ratio(), 2)
print('быстрота:', t2 - t1)
print('подобие', res*100, '%')
