print('x=t,y=t,z=t')
x = True
y = True
z = True

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=f,y=t,z=t')
x = False
y = True
z = True

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=t,y=f,z=t')
x = True
y = False
z = True

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=t,y=t,z=f')
x = True
y = True
z = False

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=f,y=f,z=t')
x = False
y = False
z = True

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=t,y=f,z=f')
x = True
y = False
z = False

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=f,y=t,z=f')
x = False
y = True
z = False

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))

print('x=f,y=f,z=f')
x = False
y = False
z = False

print(not ((x or not y) and z))
print(y or (x and not y or z))
print(not (not x and y or z))