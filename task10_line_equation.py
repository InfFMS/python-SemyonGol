# Задача 10: Уравнение прямой
# Напишите программу, которая находит значение y в уравнении прямой y = kx + b для заданных x, k и b.
# Пример:
# Ввод: k = 2, b = 3, x = 5
# Вывод: y = 13
print('Enter a coefficient of line:', end=' ')
k = int(input())
print('Enter intercept:', end=' ')
b = int(input())
print('Enter the x:', end=' ')
x = int(input())
print('y =', k*x+b)