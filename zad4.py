from simplex import simplex
from functions import f1

if __name__ == '__main__':
    x1 = [0.5, 0.5]

    for i in range(1, 21):
        print("Simplex with dx=", i)
        x = simplex(f1, x1, dx=i)
        print(x)
        print()