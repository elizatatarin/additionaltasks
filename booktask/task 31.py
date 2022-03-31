print("а")
n = float(input())  # 5
if n % 5 == 0 or n % 7 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())  # 40

if a % 10 != 0:
    print(False)
elif a % 4 == 0:
    print(True)
else:
    print(False)