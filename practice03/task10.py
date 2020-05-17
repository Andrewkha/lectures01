#  Последовательность состоит из натуральных чисел и завершается числом 0.
#  Всего вводится не более 10000 чисел (не считая завершающего числа 0).
#  Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
#  Числа, следующие за числом 0, считывать не нужно.

# Формат входных данных
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
# Формат выходных данных
#
# Выведите ответ на задачу (одно число).

max_num = 0
count = 0
while True:
    a = int(input())
    if a != 0:
        if a > max_num:
            max_num = a
            count = 1
        elif a == max_num:
            count += 1
    else:
        break

print(count)