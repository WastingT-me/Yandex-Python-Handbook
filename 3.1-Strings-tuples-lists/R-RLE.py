s = input()
if len(s) == 1:
    print(s[0], 1)
else:
    i = 0 
    char = s[0]
    s = s[1:] + 'a'
    while i < len(s):
        count = 1
        while (i < len(s)) and (s[i] == char):
            count += 1 
            i += 1
        print(char, count)
        if i < len(s):
            char = s[i]
        else:
            break
        i += 1