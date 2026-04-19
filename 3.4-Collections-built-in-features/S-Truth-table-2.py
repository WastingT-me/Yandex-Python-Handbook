from itertools import product
s = input()
var = sorted(set(char for char in s if char.isupper()))
print(' '.join(var + ['F']))
for perm in product([0, 1], repeat=len(var)):
    f = eval(s, dict(zip(var, perm)))
    print(' '.join(map(str, perm)), int(f))