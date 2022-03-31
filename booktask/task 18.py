print('x=t,y=t')
x = True
y = True

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print('x=t,y=f')
x = True
y = False

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)


print('x=f,y=f')
x = False
y = False

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)



print('x=f,y=t')
x = False
y = True

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)
