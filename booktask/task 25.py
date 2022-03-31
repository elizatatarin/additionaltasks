print('a=t,b=t,c=t')
a = True
b = True
c = True

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=f,b=t,c=t')
a = False
b = True
c = True

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=t,b=f,c=t')
a = True
b = False
c = True

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=t,b=t,c=f')
a = True
b = True
c = False

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=f,b=f,c=t')
a = False
b = False
c = True

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=t,b=f,c=f')
a = True
b = False
c = False

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=f,b=t,c=f')
a = False
b = True
c = False

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))

print('a=f,b=f,c=f')
a = False
b = False
c = False

print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and not b or not (a or not c))