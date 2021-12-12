# Подсчет комбинаторных объектов - перестановки, размещения, сочетания
# Импортируем нужные функции из модуля itertools
from itertools import permutations, combinations, combinations_with_replacement
from math import factorial

n = int(input()) # Вводим натуральное число (n >= 1)
k = int(input()) # Вводим натуральное число (k >= 1, k <= n)
iterset = range(1, n + 1) # Генерируем n-элементное множество

# Перестановки - упорядоченный набор чисел от 1 до n (порядок элементов важен)
# P(n) = n! (n-факториал)
P = list(permutations(iterset, r = n)) # перестановки длиной n из iterset

# Вывести все перестановки
# print(*P)
# Вывести количество перестановок
print(len(P))
# Или так:
print(factorial(n))
print()

# Размещения из n по k - упорядоченный набор чисел из k различных элементов n-элементного множества
# (упорядоченный набор - порядок элементов важен!)
# A(n, k) = n! / (n - k)!, (k <= n)
A = list(permutations(iterset, r = k)) # размещения длиной k из iterset

# Вывести все размещения
#print(*A)

# Вывести количество размещений
print(len(A))
# Или так:
print(factorial(n) // factorial(n - k))
print()

# Сочетания из n по k - k-элементное подмножество n-элементного множества
# (подмножество - неупорядоченный набор - порядок элементов НЕ важен)
# C(n, k) = n! / (k! * (n - k)!) = A(n, k) / P(k)
C1 = list(combinations(iterset, k)) # сочетания длиной k из iterable без повторяющихся элементов

# Вывести все сочетания без повторений
#print(*C1)

# Вывести количество сочетаний
print(len(C1))
# Или так:
print(factorial(n) // factorial(k) // factorial(n - k))
print()

# Сочетания из n по k - k-элементное подмножество n-элементного множества С ПОВТОРЕНИЯМИ
C2 = list(combinations_with_replacement(iterset, k)) # сочетания длиной k из iterset с повторяющимися элементами

# Вывести все сочетания с повторениями
print(*C2)

# Вывести количество сочетаний
print(len(C2))


# Или так:
print(factorial(n + k - 1) // factorial(k) // factorial(n - 1))
