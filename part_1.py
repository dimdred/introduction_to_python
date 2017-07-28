#дзен питона
import this

# встроеная помощь
help(help)

#все есть объект
#список методов класса ( если метод начинается c__ это специальные методы)
dir(int)
dir(1)
dir(dir)

# узнать тип объекта
type(1)
type('hello')
type(type)

# пример (ряд Фибоначчи)
n = 10
a = 0
b = 1
for i in range(n):
    temp = a
    a = b
    b += temp
    print(a)
print("Fibinacci number for {} is {}".format(n,a))