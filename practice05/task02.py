#  Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек
#  отбрасывается. Каждый год сумма вклада становится больше. Надо определить,
#  через сколько лет вклад составит не менее y рублей.
# Формат входных данных
#
# Три натуральных числа: x, p, y.
# Формат выходных данных
#
# Число лет, через сколько лет вклад составит не менее y рублей.

params = input()
params = [int(x) for x in params.split(' ')]

deposit = params[0]
interest = params[1]
limit = params[2]

year = 0

while deposit < limit:
    deposit *= 1 + interest / 100
    deposit = int(deposit * 100) / 100
    year += 1

    print(year, deposit, sep=' - ')

print(year)
