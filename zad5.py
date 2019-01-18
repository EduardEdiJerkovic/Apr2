from functions import f6
from hooke_jeeves import hooke_jeeves
import random

if __name__ == '__main__':
    e = 10 ** -4

    a = random.uniform(-50, 50)
    b = random.uniform(-50, 50)
    print(a, b)
    x = hooke_jeeves(f6, [a, b])
    print(x)
