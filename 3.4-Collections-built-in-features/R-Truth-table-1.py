from itertools import product
s = input()
print('a b c f')
for (a, b, c) in list(product([0, 1], repeat=3)):
    f = eval(s, {"a": a, "b": b, "c": c})
    print(a, b, c, int(f))