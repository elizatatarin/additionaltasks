print('a=t,b=t')
a = True
b = True

print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and a)

print('a=t,b=f')
a = True
b = False

print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and a)

print('a=f,b=f')
a = False
b = False

print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and a)

print('a=f,b=t')
a = False
b = True

print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and a)