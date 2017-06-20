def enumerate_(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

l = [1, 2, 3]
for idx, i in enumerate(l):
        print(idx, i)
print('---------------')
for idx, i in enumerate_(l):
        print(idx, i)
