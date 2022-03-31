a = False
b = False
c = True

print((not a or (not b)) and (not c))
print((not a or (not b)) and (a or b))
print(a and b or a and c or (not c))
