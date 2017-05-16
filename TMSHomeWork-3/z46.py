alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input('Введите индекс шифрования: '))
s = input('Введите текст для шифрования: ').strip()
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')
