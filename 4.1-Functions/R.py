# two pointers
def merge(c1, c2):
    c = []
    i, j = 0, 0
    lc1, lc2 = len(c1), len(c2)
    while i < lc1 and j < lc2:
        if c1[i] < c2[j]:
            c.append(c1[i])
            i += 1
        else:
            c.append(c2[j])
            j += 1
    while i < lc1:
        c.append(c1[i])
        i += 1
    while j < lc2:
        c.append(c2[j])
        j += 1
    return tuple(c)

# stack
def merge(c1, c2):
    c = []
    c1, c2 = list(c1), list(c2)
    while c1 or c2:
        if c1 and c2:
            if c1[-1] > c2[-1]:
                c.append(c1.pop())
            else:
                c.append(c2.pop())
        elif c1:
            c.append(c1.pop())
        else:
            c.append(c2.pop())
    return tuple(c[::-1])