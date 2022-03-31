print('a=t,b=t')
a = True
b = True

print(not (a and b))
print(not a or b)
print(a or not b)

print('a=t,b=f')
a = True
b = False

print(not (a and b))
print(not a or b)
print(a or not b)

print('a=f,b=f')
a = False
b = False

print(not (a and b))
print(not a or b)
print(a or not b)

print('a=f,b=t')
a = False
b = True

print(not (a and b))
print(not a or b)
print(a or not b)