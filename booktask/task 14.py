print('x=t,y=t')
x = True
y = True

print(not (x or y))
print(not x and y)
print(x and not y)

print('x=t,y=f')
x = True
y = False

print(not (x or y))
print(not x and y)
print(x and not y)


print('x=f,y=f')
x = False
y = False

print(not (x or y))
print(not x and y)
print(x and not y)


print('x=f,y=t')
x = False
y = True

print(not (x or y))
print(not x and y)
print(x and not y)
