from itertools import permutations

n = int(input())
runners = []
for i in range(n):
    runners.append(input())
for f, s, t in permutations(sorted(runners), 3):
    print(f'{f}, {s}, {t}')