##
date = int(input())
if date % 100 == 0:
    print("YES")
else:
    print("NO")
##
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())


if (a1 + a2 + b1 + b2 ) % 2 == 0:
    print("YES")
else:
    print("NO")
##
age = int(input())
male = input()

if 10 <= age <= 15 and male == "f":
    print("YES")
else:
    print("NO")
##
number = int(input())

if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("ошибка")

##
num = int(input())

if num % 2 != 0:
    print("YES")
elif num % 2 == 0 and 2 <= num <= 5:
    print("NO")
elif num % 2 == 0 and 6 <= num <= 20:
    print("YES")
elif num % 2 == 0 and num >= 20:
    print("NO")
##
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 + b1 == a2 + b2 or b1 - a1 == b2 - a2:
    print("YES")
else:
    print("NO")

##
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 - x2 == 1 and y1 - y2 == 2:
    print("YES")
elif x1 - x2 == 2 and y1 -y2 == 1:
    print("YES")
elif x1 - x2 == 2 and y1 - y2 == -1:
    print("YES")
elif x1 - x2 == 1 and y1 - y2 == -2:
    print("YES")
elif x1 - x2 == -1 and y1 - y2 == -2:
    print("YES")
elif x1 - x2 == -2 and y1 - y2 == -1:
    print("YES")
elif x1 - x2 == -2 and y1 - y2 == 1:
    print("YES")
elif x1 - x2 == -1 and y1 - y2 == 2:
    print("YES")
else:
    print ("NO")

##
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 + b1 == a2 + b2 or b1 - a1 == b2 - a2:
    print("YES")
elif a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")

