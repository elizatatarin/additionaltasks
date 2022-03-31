print("а")
a = float(input())  #9

if a % 2 == 0 or a % 3 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())  #20

if a % 10 != 0:
    print(False)
elif a % 3 != 0:
    print(True)
else:
    print(False)