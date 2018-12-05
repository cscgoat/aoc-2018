#!/usr/bin/python3

from collections import defaultdict

claim = defaultdict(int)

for line in open('03.in'):
    r = line.split(" ")
    x,y = r[2].strip(":").split(',')
    x,y = int(x), int(y)
    w,h = r[3].split('x')
    w,h = int(w), int(h)
    for i in range(w):
        for j in range(h):
            claim[(x+i, y+j)] += 1
total = 0
for (xi, yj), c in claim.items():
    if c >= 2: total += 1
print(total)


for line in open('03.in'):
    r = line.split(" ")
    idd = int(r[0].strip("#"))
    x,y = r[2].strip(":").split(',')
    x,y = int(x), int(y)
    w,h = r[3].split('x')
    w,h = int(w), int(h)
    tr = 0
    for i in range(w):
        for j in range(h):
            if claim[(x+i, y+j)] > 1: tr += 1
    if tr == 0: print(idd)

