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