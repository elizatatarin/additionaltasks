x = False
y = False
z = True

print((x or z) and (not z))
print(not x and (not y))
print(not (x and z) or y)

print(x and (not y) or z)
print(y and (not y or z))
print(x or (not (y or z)))

