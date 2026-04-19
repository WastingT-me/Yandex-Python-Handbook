s1 = input().split(', ')
s2 = input().split(', ')
for item in zip(s1, s2):
    print(f'{item[0]} - {item[1]}')