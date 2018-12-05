#!/usr/bin/python3

boxes = [line.strip() for line in open("02.in").readlines()]

a2=0; a3=0

for box in boxes:
    box = box.strip()
    ap2 = False
    ap3 = False

    for b in box:
        c = box.count(b)
        if c == 2 and not ap2: 
            a2 += 1
            ap2 = True
        elif c == 3 and not ap3:
            a3 += 1
            ap3 = True

print(a2*a3)

for box in boxes:
    for box2 in boxes:
        if box == box2: continue
        diff = 0
        same = ""
        for i in range (0, len(box)):
            if box[i] == box2[i]:
                diff += 1
                same += box[i]
        if diff == len(box) - 1:
            print(same)
            exit()
