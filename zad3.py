from functions import f4
from simplex import simplex
from hooke_jeeves import hooke_jeeves

if __name__ == '__main__':
    x4 = [5.0, 5.0]
    xmin4 = [0, 0]
    fmin4 = 0

    print("Hoock Jeeves algorithm:")
    x = hooke_jeeves(f4, x4)
    print(x)

    print("Simplex algorithm:")
    x = simplex(f4, x4)
    print(x)
