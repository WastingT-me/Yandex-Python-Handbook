from itertools import chain

s1 = input().split(', ')
s2 = input().split(', ')
s3 = input().split(', ')
for i, v in enumerate(sorted(list(chain(s1, s2, s3))), 1):
    print(f'{i}. {v}')