# recursion

def matryoshka(n):
    if n == 1:
        print('Матрёшечка')
    else:
        print(f"Top n={n}")
        matryoshka(n - 1)
        print(f"Bottom n={n}")


# Вложенные квадраты

import graphics as gr

def fractal_rectangle(A:tuple, B:tuple, C:tuple, D:tuple, window, alpha, depth=10):
    if depth < 1:
        return
    # gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    # gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    # gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, window, alpha, depth - 1)


def draw_fractal_rectangle():
    window = gr.GraphWin("Russian game", 600, 600)
    alpha = 0.2
    fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), window, alpha, 100)
    window.getMouse()
    window.close()


# draw_fractal_rectangle()

def factorial(n):
    assert n >= 0, "Not defined for negative"
    if n == 0:
        return 1
    return factorial(n - 1) * n

# print(factorial(4))

# Euqlids algorythm - наибольший общий делитель

def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b -a)

# print(gcd(35, 49))


def gcd1(a, b):
    if b == 0:
        return a
    return gcd1(b, a % b)


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


# возведение в степень
def pow(a: float, n: int):
    if n == 0:
        return 1
    return pow(a, n - 1) * a


def pow1(a: float, n: int):
    if n == 0:
        return 1
    if n % 2 == 1:
        return pow1(a, n - 1) * a
    return pow(a ** 2, n // 2)
