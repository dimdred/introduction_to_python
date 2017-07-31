import unittest

class TestStringMethods(unittest.TestCase): # класс наследуем от unittest

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

class TestDummy(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, 1)

unittest.main(exit=False) # указываем что нужно запускать как тест, без нее не работает!

# nose болкк мощное средство для тестирования (pip install nose).
# nosetest test.py
# nosetest test.py:TestDummy --  тестируем только 1 класс (можно 1 функцию или файл)! или несколько! Почитать nose

# tox - тестирование с помощью virtualenv (на новые серваки!)