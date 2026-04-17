# Reverse Polish Notation
s = input().split()
i = 0 
stack = []
while i < len(s):
    while s[i].isdigit():
        stack.append(int(s[i]))
        i += 1
    b = stack.pop()
    a = stack.pop()
    if s[i] == '+':
        stack.append(a + b)
    elif s[i] == '-':
        stack.append(a - b)
    else:
        stack.append(a * b)
    i += 1
print(stack[0])