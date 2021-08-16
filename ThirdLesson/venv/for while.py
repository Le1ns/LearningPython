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