##
for i in range(10):
    print("Python is awesome!")
##
s = input()
many = int(input())
for i in range(many):
    print(s)
##
for _ in range(6):
    print("AAA", end="\n")
for _ in range(5):
    print("BBBB", end="\n")
print("E")
for _ in range(9):
    print("TTTTT", end="\n")
print("G")

##
n = int(input())
for _ in range(n):
    print("*" * 19)

##
s = input()
for i in range(10):
    print(i, s)

##
n = int(input())
for i in range(n+1):
    print("Квадрат числа", i,"равен", i*i)
##
n = int(input())
for i in range(n+1):
    print('*' * (n-i))

##
m = float(input()) #start osobey
p = float(input()) #procent
n = int(input()) # dni


for i in range(0,n):

    print(i+1,m*(p/100+1)**i)
##
m = int(input())
n = int(input())

for i in range(m,n+1):
    print(i)
##
m = int(input())
n = int(input())
if m > n:
    for i in range(m,n-1,-1):
        print(i)
elif m < n:
    for i in range(m,n+1):
        print(i)
elif m == n:
    print(m)

##
from math import *
m = int(input())
n = int(input())
b = int(m%2+m-1)
for i in range(b, n-1, -2):
    print(i)

##
m, n = int(input()), int(input())

for i in range(m,n+1,1):
    if i % 17 ==0 or i%10 ==9 or i%15 == 0:
        print(i)
##
number = int(input())

for i in range (1,11,1):
    print(number, "x", i, '=', number*i)

##
total = 0
for i in range(1, 6):
    total += i
    print(total, end='')
##
a, b = int(input()), int(input())
total = 0
for i in range(a, b + 1):

    if i % 10 == 4 or i % 10 == 9:
        total = total + 1

print(total)

##
total = 0
for i in range(int(input())):
    temp = int(input())
    total = total + temp
print(total)
##
from math import *
temp = 1
n = int(input())
for i in range(2,n+1):
    temp = temp + (1/i)

print(temp - log(n))
##
n = int(input())
count = 0
for i in range(1, n + 1):
    temp = i * i
    if  temp %10 == 5:
        count = count + i
print(count)

##
total = 1
n = int(input())
for i in range(1,n+1):
    total = i * total
print(total)

##
temp = True
temp1 = 1
for i in range (10):
  a = int(input())
  if a == 0:
      temp = False
  else:
      temp1 = temp1 * a
print(temp1)

##
n = int(input())
sum = 0
for i in range(1,n + 1):
    if n % i == 0:
        sum = sum+i
print(sum)
##
total = 0
n = int(input())
for i in range(1, n + 1):
    total = total + pow(-1, i + 1) * i
print(total)
##
largest = 0
prelagerst = 1

for i in range(1,int(input()) +1):
    a = int(input())
    if a > largest:
        prelagerst = largest
        largest = a
    elif a < largest and a > prelagerst:
        prelagerst = a
print(largest)
print(prelagerst)
##
count = 0
for i in range(10):
    a = int(input())
    if a % 2 == 0:
        count = count +1
    else: count -1
if count == 10:
    print("YES")
else:
    print("NO")
##
n = int(input())

x = 0
for i in range(1,n + 1):
    if i <= 2:
        a = 1
        b = 1
        print(a, end=" ")
    elif i > 2:
     x = a + b
     a = b
     b = x
     print(x ,end=" ")
##WHILE
text = input()
while  text != "КОНЕЦ" and text != "конец":
    print(text)
    text = input()
##
text = input()
sum = 0
while  text != "стоп" and text != "хватит" and text != "достаточно":
    sum = sum + 1
    text = input()
print(sum)

##
numbers = int(input())
while numbers % 7 == 0:
    print(numbers)
    numbers = int(input())

##
numbers = int(input())
sum = 0
while numbers >= 0:
    sum = sum + numbers
    numbers = int(input())
print(sum)
##
stop = int(input())
sum = 0
while 0 < stop <= 5:
    if stop == 5:
        sum = sum +1
    stop = int(input())
print(sum)

##
sum = 0
cost = int(input())
while cost != 0:
    if cost >= 25:
        cost = cost - 25
        sum = sum + 1
        print(cost)
    elif 10 <= cost < 25:
        cost = cost - 10
        sum = sum + 1
        print(cost)
    elif 5 <= cost < 10:
        cost = cost - 5
        sum = sum + 1
        print(cost)
    elif 1 <= cost < 5:
        cost = cost - 1
        sum = sum + 1
        print(cost)
print(sum)


##
nu
