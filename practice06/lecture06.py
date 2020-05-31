# sorting algorithms

# сортировка вставками
def sorting_inserts(a: list):
    n = len(a)
    for top in range(1, N):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


# сортировка выбор
def choise_sort(a:list):
    n = len(a)
    for pos in range(0, n -1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


# сортировка пузырьком
def bubble_sort(a:list):
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]

