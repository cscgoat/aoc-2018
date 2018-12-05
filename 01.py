#!/usr/bin/python3

freq = [int(line.strip()) for line in open("01.in").readlines()]

print(sum(freq))

total=0; views=[]

while True:
    i = 0
    for i in range(0, len(freq)):
        total += freq[i]
        if total in views:
            print(total); exit()
        else: views.append(total)
