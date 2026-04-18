from collections import defaultdict

n = int(input())
d = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    a, b = a - a % 10, b - b % 10
    d[(a, b)] += 1
print(max(d.values()))