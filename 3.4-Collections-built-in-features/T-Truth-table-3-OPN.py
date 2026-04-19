from itertools import product

s = input()
var = sorted(set(char for char in s if char.isupper()))
print(' '.join(var + ['F']))

priority = {'not': 5, 'and': 4, 'or': 3, '^': 2, '->': 1, '~': 0}
rpn = []
stack = []
i = 0
while i < len(s):
    if s[i].isupper():
        rpn.append(s[i])
    elif s[i] == '(':
        stack.append('(')
    elif s[i] in ['n', 'o', 'a', '-', '^', '~']:
        if s[i] == 'n':
            op = 'not'
            i += 2
        elif s[i] == 'a':
            op = 'and'
            i += 2
        elif s[i] == 'o':
            op = 'or'
            i += 1
        elif s[i] == '-':
            op = '->'
            i += 1
        elif s[i] in ['^', '~']: 
            op = s[i]

        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[op]:
            rpn.append(stack.pop())
        stack.append(op)
    elif s[i] == ')':
        while stack[-1] != '(':
            rpn.append(stack.pop())
        stack.pop()
    i += 1
while len(stack) != 0:
    rpn.append(stack.pop())

for perm in product([0, 1], repeat=len(var)):
    d = dict(zip(var, perm))
    stack = []
    for token in rpn:
        if token.isupper():
            stack.append(d[token])
        elif token == 'not':
            a = stack.pop()
            stack.append(int(not a))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == 'and':
                stack.append(int(a and b))
            elif token == 'or':
                stack.append(int(a or b))
            elif token == '->':
                stack.append(int(not a or b))
            elif token == '^':
                stack.append(int((a or b) and not (a and b)))
            else:
                stack.append(int((a and b) or (not a and not b)))
    print(' '.join(map(str, perm)), stack[0])