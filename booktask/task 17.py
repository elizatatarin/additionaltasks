print('a=t,b=t')
a = True
b = True

print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print('a=t,b=f')
a = True
b = False

print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print('a=f,b=f')
a = False
b = False

print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print('a=f,b=t')
a = False
b = True

print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))