a = True
b = False
c = False

print(a or (not (a and b)) or c)
print(not a or a and (b or c))
print((a or b and not c) and c)