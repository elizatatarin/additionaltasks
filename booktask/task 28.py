print("а")
a = float(input())  # 101
b = float(input())  # 102

if a > 100 and b > 100:
    print(True)
else:
    print(False)

print("б")
a = float(input())  # 2
b = float(input())  # 5

if a % 2 == 0 and b % 2 == 0:
    print(False)
elif a % 2 == 0 or b % 2 == 0:
    print(True)
else:
    print(False)

print("в")
a = float(input())  #
b = float(input())  #

if a > 0 or b > 0:
    print(True)
else:
    print(False)

print("г")
a = float(input())  # 9
b = float(input())  # 3
c = float(input())  # 18

if a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
    print(True)
else:
    print(False)

print("д")
a = float(input())  # 96
b = float(input())  # 24
c = float(input())  # 54

if a < 50 and b < 50 and c < 50:
    print(False)
elif a < 50 or b < 50 or c < 50:
    print(True)
else:
    print(False)

print("е")
a = float(input())  # 5
b = float(input())  # -26
c = float(input())  # 55

if a < 0 or b < 0 or c < 0:
    print(True)
else:
    print(False)