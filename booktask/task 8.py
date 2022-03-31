x = False
y = True
z = False

print(x and (not (z or y)) or (not z))
print((not x or x) and (y or z))
print((x or y and (not z)) and z)