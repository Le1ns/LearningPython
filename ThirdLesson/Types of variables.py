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
