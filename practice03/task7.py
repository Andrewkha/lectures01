#  Определите сумму всех элементов последовательности, завершающейся числом 0.
#
# Числа, следующие за нулем, считывать не нужно.
# Формат входных данных
#
# Вводятся элементы последовательности по одному целому числу на строку. Числа вводятся, пока не будет введен 0.
# Формат выходных данных
#
# Вывести одно целое число - сумму последовательности.

summa = 0
while True:
    a = int(input())
    if a != 0:
        summa += a
    else:
        break

print(summa)