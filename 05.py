#!/usr/bin/python3

d = open("05.in").read().strip()

def p(d):
    while True:
        for i in range(len(d)-1):
            if d[i].lower() == d[i+1].lower() and \
            ( (d[i].islower() and d[i+1].isupper()) or \
            (d[i].isupper() and d[i+1].islower()) ):
                r = d[i] + d[i+1]
                d = d.replace(r, "", 1)
                break;
        if i == len(d)-2:
            return len(d)

print(p(d))

low = 0

for i in range(97,123):
    use = chr(i)
    f = len(d)
    temp = d.replace(use, "").replace(use.upper(),"")
    if f == len(temp): continue
    l = p(temp)
    if i == 97: low = l
    else: low = min(l,low)
print(low)
