print("а")
x = float(input())  # 69
y = float(input())  # 25

if x % 2 != 0 and y % 2 != 0:
    print(True)
else:
    print(False)

print("б")
x = float(input())  # 14
y = float(input())  # 56

if x < 20 and y < 20:
    print(False)
elif x < 20 or y < 20:
    print(True)
else:
    print(False)

print("в")
x = float(input())  # -6
y = float(input())  # 0

if x == 0 or y == 0:
    print(True)
else:
    print(False)

print("г")
x = float(input())  # -6
y = float(input())  # -9
z = float(input())  # -1

if x < 0 and y < 0 and z < 0:
    print(True)
else:
    print(False)

print("д")
x = float(input())  # 59
y = float(input())  # 5
z = float(input())  # 32

if x % 5 == 0 and y % 5 == 0 and z % 5 == 0:
    print(False)
elif x % 5 == 0 or y % 5 == 0 or z % 5 == 0:
    print(True)
else:
    print(False)

print("е")
x = float(input())  # 20
y = float(input())  # 121
z = float(input())  # 0

if x > 100 or y > 100 or z > 100:
    print(True)
else:
    print(False)
