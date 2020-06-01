# На вход программе подается последовательность чисел, заканчивающихся нулем. Сам ноль не входит в последовательность.
# Найти среднее значение последовательности. Для округления использовать функцию round(x, n). Где x - число, n -
# количество знаков после запятой.
# Формат входных данных
#
# Последовательность чисел, заканчивающихся нулем. Одно число в строку.
# Формат выходных данных
#
# Одно число — среднее значение. Округлить до двух цифр после запятой.

k = int(input())

numbers = []

while k != 0:
    numbers.append(k)
    k = int(input())

print(round(sum(numbers) / len(numbers), 2))