# Задача 7: Калькулятор с операциями
# Напишите программу, которая запрашивает у пользователя два числа и операцию (сложение, вычитание, умножение или деление) и выводит результат выполнения операции.
# Пример:
# Ввод: Первое число: 10, Второе число: 2, Операция: *
# Вывод: Результат: 20
print('Enter first number:', end=' ')
a = int(input())
print('Enter second number:', end=' ')
b = int(input())
print('Enter a sign:', end=' ')
sign = input()
if sign == '+':
    print('a + b =', a+b)
elif sign == '-':
    print('a - b =', a-b)
elif sign == '*':
    print('a*b =', a*b)
elif sign == '/':
    print('a/b =', a/b)
elif sign == '**':
    print('a^b =', a**b)
else:
    print('Error!')