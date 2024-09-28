# Задача 6: Арифметическая прогрессия
# Напишите программу, которая вычисляет n-ое число в арифметической прогрессии. Пользователь вводит первое число, шаг прогрессии и номер n.
# Пример:
# Ввод: Первое число: 2, Шаг: 3, n: 4
# Вывод: Результат: 11
print('Enter first number of progression, difference and number of members:')
a1 = int(input())
d = int(input())
n = int(input())
an = a1 + (n-1)*d
print('a', n, ' = ', an, sep='')