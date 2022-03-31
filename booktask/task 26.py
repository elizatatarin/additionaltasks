print('x=t,y=t,z=t')
x = True
y = True
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=f,y=t,z=t')
x = False
y = True
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=t,y=f,z=t')
x = True
y = False
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=t,y=t,z=f')
x = True
y = True
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=f,y=f,z=t')
x = False
y = False
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=t,y=f,z=f')
x = True
y = False
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=f,y=t,z=f')
x = False
y = True
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('x=f,y=f,z=f')
x = False
y = False
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))
