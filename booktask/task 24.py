print('x=t,y=t,z=t')
x = True
y = True
z = True

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=f,y=t,z=t')
x = False
y = True
z = True

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=t,y=f,z=t')
x = True
y = False
z = True

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=t,y=t,z=f')
x = True
y = True
z = False

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=f,y=f,z=t')
x = False
y = False
z = True

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=t,y=f,z=f')
x = True
y = False
z = False

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=f,y=t,z=f')
x = False
y = True
z = False

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

print('x=f,y=f,z=f')
x = False
y = False
z = False

print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)