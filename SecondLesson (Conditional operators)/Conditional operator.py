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
