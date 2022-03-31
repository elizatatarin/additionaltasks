a = True
b = False
c = False

print((a or b) and (not c))
print((not a) and (not b))
print(not (a and c) or b)
print(a and (not b) or c)
print(a and ((not b) or c))
print(a or (not (b and c)))



