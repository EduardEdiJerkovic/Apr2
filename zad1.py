from functions import Function
from golden_ratio import unimodal, golden_ratio

if __name__ == '__main__':
    f = Function(lambda x: (x - 3)**2)

    x0 = 10
    a, b = unimodal(f, x0)
    a, b = golden_ratio(f, a, b)
    print("For x0:", x0, "a:", a, "b:", b, "min:", (a+b)/2)

    x0 = 100
    a, b = unimodal(f, x0)
    a, b = golden_ratio(f, a, b)
    print("For x0:", x0, "a:", a, "b:", b, "min:", (a+b)/2)

    x0 = 1000
    a, b = unimodal(f, x0)
    a, b = golden_ratio(f, a, b)
    print("For x0:", x0, "a:", a, "b:", b, "min:", (a+b)/2)