s = list(map(int, input().split()))
nod = s[0]
for i in range(1, len(s)):
    if s[i] > nod:
        a, b = s[i], nod
    else:
        a, b = nod, s[i]
    while (r := a % b) != 0:
        a, b = b, r
    nod = b
print(nod)