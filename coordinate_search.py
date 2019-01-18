from golden_ratio import unimodal, golden_ratio
import math


def coordinate_search(f, x0, e=10 ** -6):
    iterations = 0
    x = x0.copy()
    while True:
        iterations += 1
        xs = x.copy()
        for i in range(len(x)):
            f.convert_to_unimodal(x, [0 if j != i else 1 for j in range(len(x))])
            a, b = unimodal(f, x[i])
            a, b = golden_ratio(f, a, b, e)
            x[i] += (a + b) / 2

        square = 0
        for i in range(len(x)):
            square += (x[i] - xs[i]) ** 2
        if math.sqrt(square) <= e:
            break
    f.convert_to_normal()
    return x, iterations
