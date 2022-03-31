print('а')
x = 1
y = -1
if x ** 2 + y ** 2 <= 4:
    print(True)
else:
    print(False)
print('б')
x = 1
y = 2
if x >= 0 or y ** 2 != 4:
    print(True)
else:
    print(False)
print('в')
x = 1
y = 2
if x >= 0 and y ** 2 != 4:
    print(True)
else:
    print(False)
print('г')
x = 2
y = 1
if x * y != 0 and y > x:
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
x = 2
y = 1
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)
print('ж')
x = 1
y = 2
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)


