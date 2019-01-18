import math


class Function:
    def __init__(self, f):
        self.f = f
        self.f_unimodal = None

    def value_of(self, x):
        if self.f_unimodal is None:
            return self.f(x)
        else:
            return self.f_unimodal(x)

    def convert_to_unimodal(self, x, v):
        self.f_unimodal = lambda l: self.f(list(map(lambda a, b: a + l * b, x, v)))

    def convert_to_normal(self):
        self.f_unimodal = None


f1 = Function(lambda x: 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2)
x1 = [-1.9, 2]
xmin1 = [1, 1]
fmin1 = 0

f2 = Function(lambda x: (x[0] - 4) ** 2 + 4 * (x[1] - 2) ** 2)
x2 = [0.1, 0.3]
xmin2 = [4, 2]
fmin2 = 0

f3 = Function(lambda x: (x[0] - 1) ** 2 + (x[1] - 2) ** 2 + (x[2] - 3) ** 2 + (x[3] - 4) ** 2 + (x[4] - 5) ** 2)
x3 = [0, 0, 0, 0, 0]
xmin3 = [1, 2, 3, 4, 5]
fmin3 = 0

f4 = Function(lambda x: abs((x[0] - x[1]) * (x[0] + x[1])) + math.sqrt(x[0] ** 2 + x[1] ** 2))
x4 = [5.1, 1.1]
xmin4 = [0, 0]
fmin4 = 0

# f6 = Function(lambda x: 0.5 + (math.sin(math.sqrt(x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2)**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2))**2))
f6 = Function(lambda x: 0.5 + (
            math.sin(math.sqrt(x[0] ** 2 + x[1] ** 2) ** 2 - 0.5) / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2))
xmin6 = (0, 0, 0, 0)
fmin6 = 0
