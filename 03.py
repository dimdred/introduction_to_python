##  Встроенные типы и синтаксис языка
# -*- coding: utf-8 -*-

# Пустое значение
None

# Логические значения
True
False

True == 1
False == 0

bool([])
bool([1])

# Числа
# Целые
1
# С плавающей запятой      
1.1

## Последовательности в Python
# Типы последовательностей:
# Изменяемые и не изменяемые

# строки
"строка", 'строка', 'hello \n world'

# сырые строки
r'hello\nworld'

# многострочные строки
"""
Hello
world
"""

# Списки List:
[1, 2, 3]
[1, [2, 'three'], 4]

# Кортежи: Tuple
(1, 'spam', 4, 'U')

# Доступ к элементу
l = [1, 2, 3]
l[0]

# Срезы: Считаются промежутки между элементами
l[1:2]
#Промежутки для списка
# 1 2 3
#^ ^ ^ ^
#0 1 2 3

#Взятие элементов в конце списка
l[-1]

# Генерация списка целых чисел
range(5)
range(3, 12, 3)

# Создание пустого списка 
empty_list = []

# Различные способы получения методов словаря
dir(list)
dir([])
dir(empty_list)

#Строки это последовательность
'hello'[0]

# Словари Dictonary:
{'food': 'spam', 'taste': 'yum'}
d = {"a": 1, "b": 2}
d["a"]

# Создание пустого словаря
d = {}
# методы словаря
dir(dict)

# Множества:
set('abc')
{'a', 'b', 'c'}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
# Пересечение
s1 & s2
# Объединение
s1 | s2
# Разность
s1 - s2
s2 - s1
# Надмножество
s1 > {1, 2}
s1 > {4, 5}

# методы множества
dir(set)

#Кортежи  
# неизменяемый тип данных
t = (1,2,3)
t[0]
t[1:2]



#модуль collections 
#дополнительные контейнеры
from collections import *
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=11, y=22) 
p2 = Point(33, 44) 
p1.x + p2.y
p1

# Представления двоичных данных: bytes, byte-array,
b'abc'
b'\x01\x02'
bytes('abc', 'ascii')
B = 'spam'.encode()
B.decode()
# bytearray изменяемая последовательность
B = bytearray('spam', 'latin1')
B[0] = 65

# Файлы:
myfile = open('02.py', 'r')
type(myfile)

# Сами типы
type(type)
type(object)


# Типы структурных элементов программ
# class, function module
import re
type(re)

# Операции над типами
dir(list)
help(list)
dir(bytes)

# Структура программы на языке Python
# Модули -> инструкции -> выражения -> объекты

a = 1
if a == 1:
    print("Good")
else:
    print("Bad")

# Несколько специальных случаев
a = 1; b = 2; print(a, b)

# Допустимо записывать одну инструкцию в нескольких

if (a == 1 and b == 2 and
    c == 3 and d == 4):  # Не забываем про двоеточие
    print('spam' * 3)

my_function(arg1,
            arg2,
            arg2)

# Обратный слеш в конце строки
a = \
    2
# но лучше использовать скобки

# Тело инструкции в одной строке
if x > y: print(x)

# Динамическая типизация
# тип имеет не переменная, а ее содержимое
a = 1
type(a)
a = 'a'
type(a)

# Разделяемые ссылки
a = 42
b = a
# имя   ссылки   объекты
# a ------------->  42
# b ----------------^
a = 'spam'
# имя   ссылки   объекты
# a -------------> 'spam'
# b ------------->  3

# функция id: уникальный идетификатор объекта (его адрес)
id(1)
# Разделяемые ссылки и изменяемые объекты
L1 = [1, 2, 3]
L2 = L1
id(L2) == id(L1)
# имя   ссылки   объекты
#  L1 -------------> [1,2,3]
#  L2 ---------------^
L1.append(4)
#  L1 -------------> [1,2,3,4]
#  L2 ---------------^
# копия списка
L2 = L1[:]
id(L2) == id(L1)
#  L1 -------------> [1,2,3,4]
#  L2 -------------> [1,2,3,4]

# Разделяемые ссылки и равенство
L2 = L1
L2 == L1
L2 is L1  # id(L2) == id(L1)

L2 = [1, 2, 3]
L2 == L1
L2 is L1

# Динамическая типизация повсюду
# Не всегда понятен тип переменной
action(enviroment, config)

## Инструкции
# Присваивание
a = 1
b = 2
a, b = b, a
a, *b = 'good', 'bad', 'ugly'
# Вызовы и другие выражения
log.write('spam, ham')
# Вызов функции
print('Spam ', joke)
# и др.

# Встроенные инструкци
# import, def, class, if, while и др.

## if
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)

# Трехместное выражение if/else
A = Y if X else Z

# while
while a > 1:  # Условное выражение
    print(a)  # Тело цикла
else:  # Необязательная часть else
    print(0)  # Выполняется, если выход из цикла производится не  инструкцией break

# break, continue, pass и else
while a > 1:
    a = a - 1
    if a % 2:
        continue  # Перейти в начало циклa
    result = action(a)
    if result:
        break  # Выйти из цикла, пропустив часть else
else:  # Выполняется, если не была использована инструкция 'break'
    print "bad action"

# for
# полный вариант
for i in range(10):  # Присваивает элементы объекта с переменной цикла
    res = action(i)
    if res > 0: break  # Выход из цикла, минуя блок else
    if res < 0: continue  # Переход в начало цикла
else:
    print("good")  # Если не была вызвана инструкция 'break'

# простой вариант
for i in range(10):
    action(i)

## Приемы программирования циклов
# Счетные циклы:  range
list(range(5))
list(range(10, 20))
list(range(5, 30, 7))
for i in range(3):
    print(i, ' Pythons')


# Генерирование индексов и элементов: enumerate
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)


# Сортировка массива
origin = 'avdsdf'
sorted(origin)
#['a', 'd', 'd', 'f', 's', 'v']
origin

## Менеджер контекста
with open('02.py') as myfile:
    for line in myfile:
        print(line)

## Логические операции
True == 1
False == 0
a = 1
b = a
a is b
a == b
a = 1

# Удобный поиск подстроки
s = 'spam'
'm' in s
# Или элемента в массиве
1 in [0, 1, 2]

bool(None)


# Утинная типизация
# если объект реализует все методы какого-то интерфейса,
# то говорят, что он реализует этот интерфейс. 

## Итераторы 
# Для унификации работы со списками содан специальный протокол.
# Объект реализующий этот протокол называется "Итератор"
# Итератор это класс реализующй методы __iter__() и __next__() 
# итераторы файлов
f = open('02.py')
f.readline()
lines = f.readlines()
# итераторы встроенных типов
L = [1, 2]
LI = iter(L)
LI.__next__()
LI.__next__()
LI.__next__()

#работа с элементами массива с помощью цикла
for l in L:
    print(l)

# Создание списков в виде инструкции
L = [i for i in range(5)]
# то же самое в виде цикла
L = []
for i in range(5):
    L.apend(i)

# список нечетных чисел
L = [i for i in range(10) if i % 2]
# то же самое в виде цикла
L = []
for i in range(5):
    if i % 2:
        L.apend(i)

# множество:
{i for i in range(5)}


# словарь:
{i: i + 1 for i in range(5)}

#с помощью цикла
d = {}
for i in range(5)
  d[i] = i + 1  


#Похоже на создание последовательностей в виде литералов
#сравните:
[0, 1, 2]
[i for i in range(3)]

{0, 1, 2}
{i for i in range(3)}

{0:1, 1:2, 2:3}
{i: i + 1 for i in range(3)}

## Общий вид генераторов
# Функции-генераторы
# Один из способов асинхронной работы
def power(start):
    print("power is called the first time")
    for i in range(start, start + 5):
        yield i * i
    print("power is called the last time")

for p in power(1):
    print(p)

# Выражения-генераторы
(i for i in range(5))


i = (i for i in range(3))
type(i)
i.__next__()
i.__next__()
i.__next__()

#Модуль itertools
from itertools import *
cycle('ABCD')
repeat(10, 3)


## Функциональные инструменты
# Генераторы списков и функция map
m = map(ord, 'spam')
dir(m)
list(m)
help(ord)

# функция filter
L = [1, 0, None, True, 2]
list(filter(bool, L))
[i for i in L if i]

# Параллельный обход: zip
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
zip(L1, L2)
list(zip(L1, L2))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)

## Полезные функции
# функция any
any(L)
# функция all
all(L)
