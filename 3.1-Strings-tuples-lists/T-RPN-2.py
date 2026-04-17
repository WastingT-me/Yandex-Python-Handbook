s = input().split()
i = 0 
stack = []
while i < len(s):
    while s[i].isdigit():
        stack.append(int(s[i]))
        i += 1
    if s[i] in {'+', '-', '*', '/'}: 
        b = stack.pop()
        a = stack.pop()
        if s[i] == '+':
            stack.append(a + b)
        elif s[i] == '-':
            stack.append(a - b)
        elif s[i] == '*':
            stack.append(a * b)
        else:
            stack.append(a // b)
    elif s[i] in {'~', '!', '#'}:
        a = stack.pop()
        if s[i] == '~':
            stack.append(-a)
        elif s[i] == '!':
            f = 1
            for j in range(1, a + 1):
                f *= j
            stack.append(f)
        else:
            stack.append(a)
            stack.append(a)     
    else:
        stack[-1], stack[-2], stack[-3] = stack[-3], stack[-1], stack[-2] 
    i += 1       
print(stack[0])