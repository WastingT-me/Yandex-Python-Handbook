def swap(a, b):
    m = min(len(a), len(b))
    for i in range(m):
        a[i], b[i] = b[i], a[i]
    if len(a) == m:
        for i in range(m, len(b)):
            a.append(b[i])
        for i in range(len(b) - m):
            b.pop()
    else:
        for i in range(m, len(a)):
            b.append(a[i])
        for i in range(len(a) - m):
            a.pop()  