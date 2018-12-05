#!/usr/bin/python3

def get_guard(text):
    return int(text.split(" ")[1].strip("#"))

def parse_time(t):
    return  int(t.split(" ")[1][3:5])

lines = [line.strip() for line in open('04.in').readlines()]
lines.sort()

guard,sleep,wake,ggg,ggf = 0,0,0,{},{}

for line in lines:
    r = line.strip().split("] ")
    date = r[0].strip("[")
    state = r[1].strip()    

    if state.startswith("Guard"):
        guard = int(get_guard(state))
    elif state.startswith("fall"):
        sleep = parse_time(date)
    elif state.startswith("wake"):
        wake = parse_time(date)
        diff = int(wake - sleep) + 1
        ggg[guard] = int(ggg.get(guard, 0)) + diff

        for mins in range (sleep, wake):
            if ggf.get(guard) == None:
                ggf.update({guard:{mins:1}});
            else:
                ggf[guard][mins] = ggf[guard].get(mins, 0) + 1;

guard=0; minute=0
for key, value in ggg.items():
    if value > minute:
        guard=key; minute=value;
#max_guard = max(ggg.keys(), key=(lambda key: ggg[key])) #optimised


freq=0; minute=0
for m, f in ggf.get(guard).items():
    if f > freq: freq = f; minute = int(m);

print(guard*minute)


guard_max = {}
for gid, obj in ggg.items():
    freq=0; minute=0;
    for m, f in ggf.get(gid).items():
        if f > freq: freq = f; minute = int(m);
    guard_max.update({gid:[minute, freq]})


guard=0; minute=0; freq=0;
for gid, obj in guard_max.items():
    if int(obj[1]) > freq:
        guard = gid
        minute = obj[0]
        freq = obj[1]

print(guard *minute)
