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


##

