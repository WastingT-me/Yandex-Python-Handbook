n = int(input())
ans = 'YES'
for i in range(n):
    s = input()
    if s[0] not in ['а', 'б', 'в']:
        ans = 'NO'
        break
print(ans)