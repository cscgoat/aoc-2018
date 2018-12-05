#!/usr/bin/python3

d = open("05.in").read().strip()

mat = {}
for i in range(97, 123):
    mat[chr(i)] = chr(i).upper()
    mat[chr(i).upper()] = chr(i)

def p(d):
    s = []
    for c in d:
        if s and c == mat[s[-1]]: s.pop()
        else: s.append(c)
    return len(s)

print(p(d))

low = 0
for i in range(97,123):
    use = chr(i)
    tmp = [c for c in d if c!=use.lower() and c!=use.upper()]
    l = p(tmp)
    if i == 97: low = l
    else: low = min(l,low)
print(low)
