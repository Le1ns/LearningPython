##
a = float(input())
b = float(input())

S = 0.5*a*b
print(S)
##
S = float(input())
V1 = float(input())
V2 = float(input())


print(S / (V1+V2))

##
a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    print(1/a)

## from farengheit to celsi
temperature = float(input())
print((5/9)*(temperature-32))

##
age = int(input())
if age == 1:
    print(10.5)
elif age == 2:
    print(21)
else:
    print(21 + (age - 2)*4)
##
number = float(input())
number = number * 10
print(int(number % 10))
##
num = float(input())
buff = int(num)
print(num-buff)

##
a = (int(input()))
b = (int(input()))
c = (int(input()))
d = (int(input()))
e = (int(input()))

maxim = max(a,b,c,d,e)
minim = min(a,b,c,d,e)

print("Наименьшее число =", minim)
print("Наибольшее число =", maxim)
##
a=int(input())
b= int(input())
c = int(input())

sum = a + b +c
maxim = max(a, b, c)
minim = min(a, b, c)

print(maxim)
print(sum-maxim-minim )
print(minim)

##
number = int(input())

a = number // 100
b = number // 10 % 10
c = number % 10
summa = a+b+c
minimum = min(a, b, c)
maximum = max(a, b, c)

middle = summa - maximum - minimum
raznost = maximum - minimum


if raznost == middle:
    print("Число интересное")
else:
    print("Число неинтересное")
##
a1, a2, a3, a4, a5 = abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input()))
print(a1+a2+a3+a4+a5)

##
p1,p2,q1,q2 = int(input()), int(input()),int(input()),int(input())
print((abs(p1-q1))+(abs(p2-q2)))

##evklidovo rasstoyanie
from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

print(sqrt(pow(x1-x2, 2) + pow(y1-y2, 2)))
##
R = float(input())
print(pi*pow(R,2))
print(2*pi*R)
##
a, b = float(input()), float(input())

sredneearifmeticheskoe = (a+b)/2
sredneeGeom = sqrt(a*b)
sredneeGarmon = (2*a*b) / (a + b)
sredreekvadrat = sqrt((pow(a,2) + pow(b,2))/2)

print(sredneearifmeticheskoe)
print(sredneeGeom)
print(sredneeGarmon)
print(sredreekvadrat)

##
x = float(input())
x = (x*pi) / 180

print(sin(x)+cos(x)+pow(tan(x), 2))

##
from math import *
x = float(input())
print(ceil(x)+ floor(x))

##
from math import *
a, b, c = float(input()), float(input()), float(input())

D = pow(b, 2) - (4 * a * c)
if D < 0:
    print("Нет корней")
elif D == 0:
    print(-(b/(2*a)))
else:
    x1 = (-b + (sqrt(pow(b,2)-(4*a*c)))) / 2*a
    x2 = (-b - (sqrt(pow(b,2)-(4*a*c)))) / 2*a
    print(min(x1, x2))
    print(max(x1, x2))

##
n, a = int(input()), float(input())
print((n*pow(a,2))/(4*tan(pi/n)))

##
print(""" "Python is a great language!", said Fred. "I don't ever remember having this much fun before." """)

##
firstname = input()
lastname = input()

print("Hello",  firstname, lastname + "!", "You just delved into Python" )
##
name = input()
print("Футбольная команда", name, "имеет длину", len(name), "символов")
##

first = input()
second = input()
third = input()

print(min(first, second, third, key=len))
print(max(first, second, third, key=len))

##
a= len(input())
b = len(input())
c = len(input())


if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print("YES")
else:
    print("NO")
##
s = input()
if 'синий' in s:
    print("YES")
else:
    print("NO")
##
s= input()
if "суббота" in s or "воскресенье" in s:
    print("YES")
else:
    print("NO")
##
s = input()
if '@' in s and '.' in s:
    print("YES")
else:
    print("NO")
## 7.1 for
for i in range(10):
    print("Python is awesome!")

##
s = input()
many = int(input())
for i in range(many):
    print(s)

###
for _ in range(6):
    print("AAA", end="\n")
for _ in range(5):
    print("BBBB", end="\n")
print("E")
for _ in range(9):
    print("TTTTT", end="\n")
print("G")

###
n = int(input())
for _ in range(n):
    print("*" * 19)

###
s = input()
for i in range(10):
    print(i, s)

###
n = int(input())
for n in range(n+1):
    print("Квадрат числа", n,"равен", n*n)

##
n = int(input())
for i in range(n+1):
    print('*' * (n-i))

###
m = float(input()) #start osobey
p = float(input()) #procent
n = int(input()) # dni

for i in range(0,n):
    print(i+1,m*(p/100+1)**i)

### 7.2
m = int(input())
n = int(input())

for i in range(m,n+1):
    print(i)
###
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

###
m, n = int(input()), int(input())

for i in range(m,n+1,1):
    if i % 17 ==0 or i%10 ==9 or i%15 == 0:
        print(i)
###
number = int(input())

for i in range (1,11,1):
    print(number, "x", i, '=', number*i)

##7.5
num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

##
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit, end="")
    num = num // 10

##
total = 0
largest = 0
smallest = 9
n = int(input())
while n != 0:
    total = n % 10
    if total <= smallest:
        smallest = total
    if total >= largest:
        largest = total

    n=n // 10
print("Максимальная цифра равна", largest)
print("Минимальная цифра равна", smallest)

##
total = 0
sum = 0
number = 0
proizvedenie = 1
srednee = 0
firstnum = 0

chislo = int(input())
firstnum = chislo
lastnum = chislo % 10
while chislo != 0:
    total = chislo % 10
    sum = sum + total
    proizvedenie = proizvedenie * total
    number = number + 1
    chislo = chislo // 10
firstnum = firstnum // (pow(10,(number - 1)))
srednee = sum / number
sumfl = firstnum + lastnum
print(sum,number,proizvedenie,srednee,firstnum,sumfl, sep="\n")

##
n = int(input())

while n > 9:
    number = n % 10 #get last
    n = n // 10 #get part without last
print(number)

##
n = int(input())
flag = 0
last_digit = n % 10
while n != 0:
    j = n % 10
    if last_digit != j:
        flag = flag + 1
    n = n // 10
if flag == 0:
    print("YES")
else:
    print("NO")
##
n = int(input())
flag = 0
while n > 9:
    last_digit = n % 10
    n = n // 10
    prelast_digit = n % 10
    if prelast_digit < last_digit:
        flag = flag + 1
if flag == 0:
    print("YES")
else:
    print("NO")

##7.6
n = int(input())
for i in range(2, n+1):
    if n % i == 0:
        break
print(i)
