x = True
y = False
z = False

print(not x or (not y) or (not z))
print((not x or (not y)) and (x or y))
print(x and y or x and z or (not z))