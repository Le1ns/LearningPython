##
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')
##
i=int(input())
if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

##1 password
first, second = input(), input()
if first == second:
    print("Пароль принят")
else:
    print("Пароль не принят")
##2 chetnoe ne chetnoe

number = int(input())
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

##3
number = int(input())
a = number // 1000
b = (number // 100) % 10
c = (number % 100) // 10
d = (number % 1000) % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")
##4 18 >= age
age = int(input())

if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


##5 arifmetic progression

number1, number2, number3 = int(input()), int(input()), int(input())
if number1 - number2 == number2 - number3:
    print("YES")
else:
    print("NO")
##6 > <
number1, number2, number3, number4 = int(input()), int(input()), int(input()), int(input())
ab = 0
cd = 0
if number1 > number2:
    ab = number2
else:
    ab = number1
if number3 > number4:
    cd = number4
else:
    cd = number3
if ab > cd:
    print(cd)
else:
    print(ab)
##7 age
age = int(input())
if age <= 13:
    print("детство")
else:
    if 14 <= age <= 24:
        print("молодость")
    else:
        if 25 <= age <= 59:
            print("зрелость")
        else:
            if age >= 60:
                print("старость")

##
number1, number2, number3 = int(input()), int(input()), int(input()),
sum = 0
notplus = 0
if number1 > 0:
    sum = sum + number1
else:
    notplus = notplus + 1
if number2 > 0:
    sum = sum + number2
else:
    notplus = notplus + 1
if number3 > 0:
    sum = sum + number3
else:
    notplus = notplus + 1
if notplus == 3:
    print(0)
else:
    print(sum)
#logical operations

##1
num = int(input())
if -1 < num < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

##
point = int(input())
if point <= -3 or point >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

##
point = int(input())
if -30 < point <= -2 or 7 < point <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")
##
numer = int(input())
if 999 < numer < 10000 and (numer % 7 == 0 or numer % 17 == 0):
    print("YES")
else:
    print("NO")
##triangle
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and c + b > a:
    print("YES")
else:
    print("NO")
##

year = int(input())
print(year % 4)
print(year % 400)
print(year % 100)
if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
    print("YES")
else:
    print("NO")
##chakemate lodiya
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (0 < a  < 9 and 0 < b < 9 and 0 < c < 9 and 0 < d < 9) and (a == c or b == d):
    print("YES")
else:
    print("NO")
##chakemate king
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (0 < a < 9 and 0 < b < 9 and 0 < c < 9 and 0 < d < 9) and (a-1 <= c <= a+1 and b - 1 <= d <= b+1):
    print("YES")
else:
    print("NO")


#############Nested and cascading conditions

