s = input()
ans = 'YES'
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        ans = 'NO'
        break
print(ans)