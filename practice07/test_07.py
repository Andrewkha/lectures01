#  На вход программе подается массив чисел.Необходимо найти число, которое чаще всего встречается в массиве.
#  Гарантируется, что такое число одно.
# Формат входных данных
#
# В первой строке задается число N , длина массива, далее идут N чисел -- элементы массива.
# Все числа больше 0 и меньше 100. Каждое число вводится с новой строки.
# Формат выходных данных
#
# Одно число, которое встречается наибольшее количество раз.

length = int(input())

numbers = []

for _ in range(length):
    numbers.append(int(input()))

m = numbers[0]
max_count = 1
for pos in range(length):
    curr = numbers[pos]
    count = 1
    for next_pos in range(pos + 1, length):
        if curr == numbers[next_pos]:
            count += 1
    if count > max_count:
        m = curr
        max_count = count

print(m)


# numbers = [417, 34,30,20,52,30,2,64,54,30,5,92,60,5,77,2,62,60,24,5,56,56,7,2,5,52,92,2,20,54,30,60,30,42,56,92,5,42,
#            36,5,64,36,56,41,34,30,34,52,34,30,64,56,52,36,5,56,64,64,60,24,42,64,42,62,54,24,30,34,92,64,8,20,92,92,5,56,
#            56,41,77,2,5,24,24,41,30,5,52,8,30,5,2,62,56,5,92,7,5,30,42,56,64,34,92,2,41,2,42,42,54,56,64,20,34,30,62,
#            34,34,64,34,77,30,34,2,60,92,34,52,24,34,64,92,24,56,62,62,54,8,64,52,30,52,2,2,42,64,34,2,74,42,42,60,20,64,
#            77,60,34,5,77,42,92,64,5,64,5,34,2,56,56,5,62,30,42,30,20,77,56,60,7,56,20,54,30,54,24,24,34,92,30,20,7,64,24,
#            41,41,42,5,2,77,64,56,30,2,92,2,56,20,64,77,64,56,77,62,56,42,30,64,54,77,52,42,52,77,92,62,54,77,77,42,56,2,
#            30,54,56,2,77,56,52,34,2,42,77,5,34,77,41,56,30,30,54,64,64,5,60,41,7,2,64,5,24,92,56,30,42,42,56,77,2,8,92,
#            8,56,5,5,34,2,56,24,5,20,64,52,34,42,30,64,34,7,42,64,56,30,56,2,52,56,34,54,77,77,30,30,5,2,64,2,34,5,52,62,
#            34,41,64,64,60,41,64,34,30,24,36,52,34,2,64,8,30,56,54,5,42,34,64,52,60,60,34,77,2,42,56,8,2,34,42,24,62,8,
#            42,54,62,52,92,56,7,92,20,92,52,52,60,2,42,42,42,34,7,56,2,42,30,77,56,20,64,42,42,64,52,42,8,42,36,34,52,30,
#            5,64,30,62,56,20,34,92,54,24,42,5,52,34,20,52,24,64,64,42,54,24,42,74,52,77,30,62,20,64,34,56,2]
# dct = {}
#
# for one in numbers:
#     if one in dct.keys():
#         dct[one] += 1
#     else:
#         dct[one] = 1
#
# print(dct)
# m = numbers[0]
# max_count = 1
# for pos in range(len(numbers)):
#     curr = numbers[pos]
#     count = 1
#     for next_pos in range(pos + 1, len(numbers)):
#         if curr == numbers[next_pos]:
#             count += 1
#     if count > max_count:
#         m = curr
#         max_count = count
#
# print(m)

