print('We are learning pyton')
print()
print("one", 'two', "Three")
print("i want to use 'test' for looking kovichki")
print('i want to see "kovichki"')
# 1
print("Здравствуй, мир!")
# 2
print("4", "8", "15", "16", "23", "42")
# 3
print("4")
print("8")
print("15")
print("16")
print("23")
print("42")
# 4
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
##########################
""" Teory
print('how are u?')
name = input()
print('hello', name)

############################
name=input("What is ur name?" )
print("my name is", name)
"""
# Input #1
##
name = input()
print("Привет,", name)
##2
name = input()
print(name, "- чемпион!")
##3
first = input()
second = input()
third = input()
print(first)
print(second)
print(third)
##4
first = input()
second = input()
third = input()
print(third)
print(second)
print(first)
##
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')

##1
print("I", "like", "Python", sep="***")
##2
delim=input()
first=input()
second=input()
third=input()
print(first, second, third, sep=delim)
##3
name = input()
print("Привет,", name, end="!")
##################################
"""
Celochislennie znacheniya
"""
##1
count = int(input())
print(count)
print(count + 1)
print(count + 2)
##2
first = int(input())
second = int(input())
third = int(input())
print(first + second + third)
##3
long = int(input())
print("Объем =", long*long*long)
print("Площадь полной поверхности =", 6*long*long)
##4
a = int(input())
b = int(input())
print(3*((a+b)**3)+275*(b**2)-127*a-41)
##5
chislo = int(input())
print("Следующее за числом", chislo, "число:", chislo+1)
print("Для числа", chislo, "предыдущее число:", chislo-1)
##6
first = int(input())
second = int(input())
third = int(input())
four = int(input())

print((first+second+third+four)*3)
##7
a = int(input())
b = int(input())

print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
##8
a = int(input())
b = int(input())
n = int(input())
an = a + b*(n - 1)
print(an)

###9
number = int(input())
print(number, 2*number, 3*number, 4*number, 5*number, sep="---")
"""
Arifmetika
part 2
"""
##1
b = int(input())
q = int(input())
n = int(input())
bn = b * q ** (n-1)
print(bn)
##2 Напишите программу, которая находит полное число метров по заданному числу сантиметров.
santi = int(input())
metr = santi // 100
print(metr)
##3  n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
n = int(input())
k = int(input())
dost = k // n
ost = k % n
print(dost)
print(ost)
##4 Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.
"""
Формат входных данных
На вход дается число целое n – население Вселенной.

Формат выходных данных
Программа должна вывести одно число – количество выживших.
"""
people = int(input()) + 1
print(people // 2)
##5
mesto = int(input())
print(-(mesto // -4))
##6
min = int(input())
hour = min // 60
minuten = min % 60
print(min, "мин - это", hour, "час", minuten, "минут.")

##7
number = int(input())
a = number % 10
b = (number % 100) // 10
c = number // 100

print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)
##7
number = int(input())
c = number % 10
b = (number % 100) // 10
a = number // 100
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")
##8
number = int(input())
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10

print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)

