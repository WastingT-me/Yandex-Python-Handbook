from sys import stdin

for line in stdin:
    if '#' not in line:
        print(line.rstrip("\n"))
    else:
        if line[0] != '#':            
            print(line[0:line.find('#')])