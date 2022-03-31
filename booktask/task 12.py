print('а')
x = 1
y = -1
if x ** 2 - y ** 2 <= 0:
    print(True)
else:
    print(False)
print('б')
x = 2
y = -2
if x >= 2 or y ** 2 != 4:
    print(True)
else:
    print(False)
print('в')
x = 2
y = 2
if x >= 0 and y ** 2 > 4:
    print(True)
else:
    print(False)
print('г')
x = 1
y = 2
if x * y != 4 and y > x:
    print(True)
else:
    print(False)
print('д')
x = 2
y = 1
if x * y != 0 and y < x:
    print(True)
else:
    print(False)
print('е')
x = 1
y = 2
if not x * y < 1 and y > x:
    print(True)
else:
    print(False)
print('ж')
x = 2
y = 1
if not x * y < 0 or y > x:
    print(True)
else:
    print(False)


