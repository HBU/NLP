# print absolute value of an integer:
a = -100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
   line2
   line3''')
print('''line1
line2
line3''')

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('包含中文的str')

print('%2d-%03d' % (3, 1))
print('%.2f' % 3.1415926)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))