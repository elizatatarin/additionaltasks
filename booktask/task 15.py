print('a=t,b=t')
a = True
b = True

print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print('a=t,b=f')
a = True
b = False

print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print('a=f,b=f')
a = False
b = False

print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print('a=f,b=t')
a = False
b = True

print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)