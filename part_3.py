# ввод вывод
# Ввод текста в консоли
i = input("text:")

# Использование текста
print(i, int(i)*2)

# форматированный вывод
# примеры: безномерный, номерной именованный

i = 1
'I have ' + str(i) + ' apple'

# функция FORMAT основной способ форматирования
'I have {} apples and {} bananas'.format(3,2)
'I have {1} apples and {0} bananas'.format(3,2)
'I have {apple} apples and {banan} bananas'.format(apple=3,banan=2)

# Если нужны сложные стуктуры:
# string.Template.template
jinja2 # шаблонизатор вывода (готовые примеры)

# Старый вариант с использованем % (лучше использовать новый!)
'I have %i apples' %2


# Использование функции print() Во 2ой версии print оператор!
# print(*object, sep='', end='\n', file=sys.stdout, flush=False) можно писать сразу в файл(не нужно предварительное открытие)flush - сбрасывание буфера
print(1,2,3)
print(1,2,3, sep='-')

print(1,2,3, sep='-', end=';')

# все строки в юникоде
# кодировка входных файлов разная
# строки можно кодировать
a = "abc абв".encode('cp1251')

# обратно
b'abc \xe0\xe1\xe2'.decode('cp1251')

# открытие файла
# текстовые файлы
# open() открывает файл и возвращает "файл подобный" объект
f = open('test1.txt')
type(f)

# открытие файла с кодировкой
# можно указать кодировку при чтении/записи в текстовом режиме

f = open('test.txt', encoding='cp1251')
# чтение строки
f.readline()
# чтение всего файла в одну строку
f.read() # читаем по указателю
f.seek(0) # передвигаем указатель откуда читать
# чтение в список (по указателю)
f.readlines()
# закрытие файла, когда он больше не нужен
f.close()

f = open('test.txt', encoding='utf8')  # кодировка по умолчанию utf8
f.readline()
f.close()

# работа с каждой строкой. Использовать для больших файлов. Не занимаем память.
for line in open("test.txt"):
    print(line.strip()) # strip - отрезаем символ перевода строки и пустые пробелы в начале

# запись в файл
f = open('test1.txt', 'w') # w-создать для записи
f.write("Test\n")
f.write("Check")
# печать в файл
print("text", file=f)
f.close()

# менеджер контекста
with open('test2.txt', 'w') as file:
    file.write('Spam and eggs!')

# бинарный файл
with open('test_bin.txt', 'wb') as file:
        #file.write(b'abc \xe0\xe1\xe2')
        file.write('Привет'.encode('cp1251'))
        file.write(b'Hello')

# загрузка из бинароного файла
fb = open('test_bin.txt', 'rb')
fb.read()

fr = fb.read()
fr.decode(encoding='cp1251')
fb.close()

# модуль stuct загрузка структурированных данных
import struct
# экспорт данных
struct.pack('IH',1,2)
struct.unpack('IH', buf)



## Идиомы Python
# проверка истиности для множеств
# if x:
# if no x:
# Good!
name = 'Safe'
pets = ['Dog', 'Cat', 'Hamster']
owners = {'Safe': 'Cat', 'George': 'Dog'}
# определяем есть ли данные в 3 переменных, пустые переменные False a=[]
if name and pets and owners:
    print('We have pats!')

# неправильный путь для пайтона!!!
if name != '' and len(pets) > 0 and owners != {}:
    print('We have pats!')

# Использование выражений 'in': if x in iyems:
# GOOD
name = 'Safe Hammad'
if 'H' in name:
    print('This name has an H in it')

# NOT GOOD
name = 'Safe Hammad'
if name.find('H') != -1: # find возвращает позиция, если -1 то не найден!
    print('This name has an H in it')

# for x in items:
# GOOD
pets = ['Dog', 'Cat', 'Hamster']
pet = 'Dog'
for pet in pets:
    print('A {} pet can be very cute!'.format(pet))
pet in pets


# Обмен значениями переменных
a, b = b, a

## Объединение списков в строку:
# GOOD!

chars = ['S', 'a', 'f', 'e']
name =''.join(chars)
print(name)
name ='-'.join(chars)  # '-' - разделитель!
print(name)

# NOT GOOD! Медленно!!!
chars = ['S', 'a', 'f', 'e']
name = ''
for char in chars:
    name += char
print(name)

## Использовать enumerate: for i, item in enumerate(items):
# GOOD
# узнать индекс элемента в массиве
names = ['Safe', 'George', 'Mildred']
for i, name in enumerate(names):
    print(i, name) # 0 Safe, 1 George

# NOT GOOD
names = ['Safe', 'George', 'Mildred']
count = 0
for name in names:
    print(i, name)
    count += 1

# Использование генераторов списков
# GOOD!

data = [5, 7, 3, 11, 15]
result = [i * 3 for i in data if i > 10] # проверка списка по условию и новый список!
print(result)

# NOT GOOD!!
data = [5, 7, 3, 11, 15]
result = []
for i in data:
    if i > 10:
        result.append(i*3)
print(result)

# Создание словарей с помощью zip dict(zip(keys,values)
# GOOD!
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = dict(zip(keys,values))
print(d)

d.keys() # список ключей
d.values() # список значений

#NO GOOD!
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = {}
for i, key in enumerate(keys):
    d[keys] = values[i]
print(d)

# Использовать _ для ненужных (отбрасываемых) переменных
for k, _ in [('a', 1), ('b', 2), ('c', 3)] # когда работаем со списком из 3х элементов и 2ой ненужен!

## Использование dict.get() and dict.setdefault()
d = {'a': 1, 'b': 2}
d.get('a')
d.get('c') # значение None
d['c'] # вернет ошибку, несуществуюющий индекс
d.setdefault('c',3) # применять для добавления значений в словарь
d['c']

## Сортировка списков
# метод объекта: sort: сортировка на месте

l = [2, 5, 1, 8, 3]
l.sort()
l.sort(key=fun) # по умолчанию по мере возрастания, но можно написать свою функцию сравнения# в для объектов

l = [2, 5, 1, 8, 3]
sorted(l) #функция возвращает отсортированный список не перезаписывая его (временно)

reversed(l) # список не изменный
list(reversed(l))
l.reverse() # список перезаписывается

## Документация кода
# docstring
def f():
    '''Description of function!'''
    pass

help(f) # получим описание функции! поэтому сложные функции нужно описывать!

#sphinx для красивой документации с отчетами

# профилирование и отладка!
# time
# вычисляем сколько отработала прога
import time
start = time.time()
time.sleep(4)
# or do something more productive!
done = time.time()
elapsed = done - start
print(elapsed)


# проверка сколько работает алгоритм! (запускает несколько раз и среднее показывает!)
# timeit
import timeit
t1 = timeit.Timer("text='sample string'; char = 'g'; char in text")
t1.timeit()
# 0.053

def s(text, char):
    for c in text:
        if c == char:
            return True
    return False
t2 = timeit.Timer("s('sample string', 'g')", setup='from __main__ import s')
t2.timeit()
# 0.74

# вызов из коммандной строки
# python -m timeit -s "text = \"sample string\"; char = \"g\"" "char in text"

# profile
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

# отладка: ставим точки прерывания и Debug (IDE)

# pdb используем если нету средств отладки (удаленно на серваке)
import pdb
pdb.set_trace()

# debug.py ранать из консоли!
import pdb; pdb.set_trace()

##  ТЕстирование кода!
# test.py

import unittest

class TestStringMethods(unittest.TestCase): # класс наследуем от unittest
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('Foo'.isupper())

class TestDummy(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, 1)

unittest.main(exit=False)

# unittest.mock
# можем подменить любой объект в классе!

from unittest.mock import MagicMock
class ProductionClass():
    def method(self):
        pass # заглушка, класс ничего не возвращает

thing = ProductionClass()
thing.method = MagicMock(return_value=3) # будем возвращать 3 в методе
thing.method(3, 4, 5, key='value')
# вернет 3

thing.method.assert_called_with(3, 4, 5, key='value')
# проверим с какими параметрами вызван метод, если - (3, 4, 4, key='value') то ошибку вернет

# patch
# заменяет метод в классе! похож на  mock
with unittest.mock.patch.object(ProductionClass, 'method', return_value=None) as mock_method1:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method1.assert_called_once_with(1, 2, 3)
mock_method1.assert_called_once_with(1, 2, 4)

# patch и mock гибко подменять чтото или проверять правильно ли вызванны объекты. удобно для написания юнит тестов