from operator import add
from random import shuffle
from collections import Counter

def p():
    r = list(range(4))
    shuffle(r)
    return r

def process(tab,rounds):
    for i in range(rounds):
        tab = sorted(map(add,tab,[x for y in [p() for i in range(int(len(tab)/4))] for x in y]))
    return tab

def main():
    t = int(input("Number of rooms: ")) * 4
    r = int(input("Number of rounds: "))
    f = int(input("Number of breaking teams: "))
    n = int(input("Number of iterations (recommended 1000+): "))
    s = [process([0 for i in range(t)],r) for i in range(n)]
    m = [[list(set(br[-f:]))[0]] for br in s]
    p = [(m[i][0],s[i][-f:].count(m[i][0]),s[i].count(m[i][0])) for i in range(len(m))]
    d = dict(Counter(p))
    for x in sorted(d.keys(), key = lambda x: -d[x]):
        print(str(x[1])+"/"+str(x[2])+" on "+str(x[0])+" points: "+str(round((d[x]/n)*100,3))+"%")
