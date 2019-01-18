from hooke_jeeves import hooke_jeeves
from functions import f1, f2, f3, f4
from functions import x1, x2, x3, x4
from coordinate_search import coordinate_search
from simplex import simplex

if __name__ == '__main__':
    print("Start for f1 ---------------------------")
    xmin1 = [1, 1]
    fmin1 = 0

    print("Hoock Jeeves algoritm:")
    x = hooke_jeeves(f1, x1)
    print(x)

    print("Coordinate search algorith:")
    x = coordinate_search(f1, x1)
    print(x)

    print("Simplex algorithm:")
    x = simplex(f1, x1)
    print(x)

    print("Start for f2 ---------------------------")
    xmin2 = [4, 2]
    fmin2 = 0

    print("Hoock Jeeves algoritm:")
    x = hooke_jeeves(f2, x2)
    print(x)

    print("Coordinate search algorith:")
    x = coordinate_search(f2, x2)
    print(x)

    print("Simplex algorithm:")
    x = simplex(f2, x2)
    print(x)

    print("Start for f3 ---------------------------")
    xmin3 = [1, 2, 3, 4, 5]
    fmin3 = 0

    print("Hoock Jeeves algoritm:")
    x = hooke_jeeves(f3, x3)
    print(x)

    print("Coordinate search algorith:")
    x = coordinate_search(f3, x3)
    print(x)

    print("Simplex algorithm:")
    x = simplex(f3, x3)
    print(x)

    print("Start for f4 ---------------------------")
    xmin4 = [0, 0]
    fmin4 = 0
    print("Hoock Jeeves algoritm:")
    x = hooke_jeeves(f4, x4)
    print(x)

    print("Coordinate search algorith:")
    x = coordinate_search(f4, x4)
    print(x)

    print("Simplex algorithm:")
    x = simplex(f4, x4)
    print(x)
