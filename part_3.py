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