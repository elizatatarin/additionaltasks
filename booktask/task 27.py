print("а")
x = float(input())  # 3
y = float(input())  # 4

if x > 2 and y > 3:
    print(True)
else:
    print(False)

print("б")
x = float(input())  # 2
y = float(input())  # 4

if x > 1 or y > -2:
    print(True)
else:
    print(False)

print("в")
x = float(input())  # 0
y = float(input())  # 6

if x >= 0 and y > 5:
    print(True)
else:
    print(False)

print("г")
x = float(input())  # 4
y = float(input())  # -3

if x > 3 or y < -1:
    print(True)
else:
    print(False)

print("д")
x = float(input())  # 4
y = float(input())  # 9

if x > 3 and y < 10:
    print(True)
else:
    print(False)

print("е")
x = float(input())  # 1

if not x > 2:
    print(True)
else:
    print(False)

print("ж")
x = float(input())  # 1

if not x > 2 and x < 5:
    print(True)
else:
    print(False)

print("з")
x = float(input())  # 20


if 10 < x and x <= 20:
    print(True)
else:
    print(False)

print("и")
x = float(input())  # 4
y = float(input())  # 4

if 0 < y <= 4 and x < 5:
    print(True)
else:
    print(False)