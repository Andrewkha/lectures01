#  Вводится последовательность, состоящая только из 0 и 1. Необходимо найти максимальное количество 1,
#  идущих подряд (без 0 между ними).
# Формат входных данных
#
# В первой строке задается натуральное N<=10000 , длина массива, далее идут N чисел 0 или 1 -- элементы массива.
# Каждое число вводится с новой строки.
# Формат выходных данных
#
# Одно число — результат.

len = int(input())
count = 0
largest_count = 0

for k in range(len):
    a = int(input())
    if a == 1:
        count += 1
    else:
        if count > largest_count:
            largest_count = count
        count = 0

print(largest_count if largest_count > count else count)