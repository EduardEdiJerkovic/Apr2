import math

k = 0.5 * (math.sqrt(5) - 1)


def golden_ratio(f, a, b, e=10 ** -6):
    if a > b:
        raise ValueError("ERROR: 01\nInterval values should be from lover to higher value.")
    c = b - k * (b - a)
    d = a + k * (b - a)
    fc = f.value_of(c)
    fd = f.value_of(d)
    while (b - a) > e:
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = f.value_of(c)
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = f.value_of(d)
    return a, b


def unimodal(f, point, h=1):
    l = point - h
    r = point + h
    m = point
    step = 1

    fm = f.value_of(point)
    fl = f.value_of(l)
    fr = f.value_of(r)

    if fm < fr and fm < fl:
        return l, r
    elif fm > fr:
        while True:
            l = m
            m = r
            fm = fr
            step *= 2
            r = point + h * step
            fr = f.value_of(r)
            if not fm > fr:
                break
    else:
        while True:
            r = m
            m = l
            fm = fl
            step *= 2
            l = point - h * step
            fl = f.value_of(l)
            if not fm > fl:
                break

    return l, r
