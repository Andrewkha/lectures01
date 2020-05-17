# Дано трехзначное число. Найдите сумму его цифр.
# Формат входных данных
#
# Вводится трехзначное число.
# Формат выходных данных
#
# Одно число — сумма цифр


def sum_digits(number):
    ones = number % 10
    number = number // 10
    tens = number % 10
    number = number // 10

    return ones + tens + number
