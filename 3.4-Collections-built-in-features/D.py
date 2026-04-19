from itertools import accumulate
s = input().split()
for word in accumulate(s, lambda x, y: x + ' ' + y):
    print(word)