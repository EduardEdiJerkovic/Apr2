from hooke_jeeves import hooke_jeeves

f = lambda x: (x - 3)**2

"""
a, b = unimodal_single_variable(f, 10, 0.125)
print(a, b)
a, b = golden_ratio_single_variable(f, a, b, 0.05)
print(a, b)
print((a + b) / 2)
print(f((a+b) / 2))
"""
"""
f2 = lambda x: (x[0] - 4)**2 + 4 * (x[1] -git 2)**2
x = [0.1, 0.3]
lst = unimodal_multiple_variables(f2, x, 0.125)
print(lst)
result = golden_ratio_multiple_variables(f2, lst, 10**-6)
print(result)

print(f2([(result[0][0] + result[0][1])/2, (result[1][0] + result[1][1])/2]))


r = hooke_jeeves(f2, x, 0.5, 10**-6)
print(r)
"""
