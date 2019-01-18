import math


def simplex(f, x0, a=1, b=0.5, g=2, dx=1, e=10 ** -6):
    xc = []
    xl = []
    iterations = 0
    points = []
    for i in range(len(x0)):
        points.append([x0[j] if j != i else x0[j] + dx for j in range(len(x0))])
    while True:
        xh, xl, h = get_min_max(f, points)
        xc = find_centroid(f, points, h)
        xr = reflection(xc, xh, a)

        if f.value_of(xr) < f.value_of(xl):
            xe = expansion(xc, xr, g)
            if f.value_of(xe) < f.value_of(xl):
                xh = xe.copy()
            else:
                xh = xr.copy()
        else:
            flag = True
            for j in range(len(points)):
                if f.value_of(xr) <= f.value_of(points[j]) and j != h:
                    flag = False
                    break
            if flag:
                if f.value_of(xr) < f.value_of(xh):
                    xh = xr.copy()
                xk = contraction(xc, xh, b)
                if f.value_of(xk) < f.value_of(xh):
                    xh = xk.copy()
                else:
                    for i in range(len(points)):
                        points[i] = [(points[i][j] + xl[j]) / 2 for j in range(len(points[i]))]
            else:
                xh = xr.copy()
        points[h] = xh.copy()

        square = 0
        iterations += 1
        for i in range(len(xh)):
            square += (xh[i] - xc[i]) ** 2
        if math.sqrt(square) <= e:
            break

    return xc, iterations


def get_min_max(f, points):
    h = (0, f.value_of(points[0]))
    l = (0, f.value_of(points[0]))
    for i in range(len(points)):
        if f.value_of(points[i]) > h[1]:
            h = (i, f.value_of(points[i]))
        elif f.value_of(points[i]) < l[1]:
            l = (i, f.value_of(points[i]))

    return points[h[0]], points[l[0]], h[0]


def find_centroid(f, points, h):
    xc = [0] * (len(points[0]))
    for i in range(len(points)):
        if i == h:
            continue
        for j in range(len(points[i])):
            xc[j] += points[i][j]
    xc = [c / (len(xc) - 1) for c in xc]
    print("centroid:", xc, "function value:", f.value_of(xc))
    return xc


def reflection(xc, xh, a):
    return [xc[i] + a * (xc[i] - xh[i]) for i in range(len(xc))]


def contraction(xc, xh, b):
    return [xc[i] + b * (xh[i] - xc[i]) for i in range(len(xc))]


def expansion(xc, xr, g):
    return [xc[i] + g * (xr[i] - xc[i]) for i in range(len(xc))]
