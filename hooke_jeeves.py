def hooke_jeeves(f, x0, dx=0.5, e=10 ** -6):
    iterations = 0
    xp = x0.copy()
    xb = x0.copy()
    while True:
        iterations += 1
        xn = find(f, xp, dx)
        if f.value_of(xn) < f.value_of(xb):
            xp = list(map(lambda n, b: 2 * n - b, xn, xb))
            xb = xn.copy()
        else:
            dx /= 2
            xp = xb.copy()
        if dx <= e:
            return xb, iterations


def find(f, xp, dx):
    x = xp.copy()
    for i in range(len(xp)):
        P = f.value_of(x)
        x[i] += dx
        N = f.value_of(x)
        if N > P:
            x[i] -= 2 * dx
            N = f.value_of(x)
            if N > P:
                x[i] += dx
    return x
