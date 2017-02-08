from operator import add
from collections import Counter
from itertools import chain
from random import shuffle

def gen(shufflee = list(range(4))):
    shuffle(shufflee)
    return shufflee

def process(tab,rounds,rm):
    for i in range(rounds):
        tab = sorted(list(map(add,tab,list(chain(*[gen() for i in range(rm)])))))
    return sorted(tab)

def main():
    rm = int(input("Number of rooms: "))
    r = int(input("Number of rounds: "))
    f = int(input("Number of breaking teams: "))
    n = int(input("Number of iterations (recommended 1000+): "))
    s = [process([[0]*rm*4][0],r,rm) for i in range(n)]
    m = [list(set(br[-f:]))[0] for br in s]
    p = [(m[i],s[i][-f:].count(m[i]),s[i].count(m[i])) for i in range(len(m))]
    d = dict(Counter(p))
    for x in sorted(d.keys(), key = lambda x: -d[x]):
        print(str(x[1])+"/"+str(x[2])+" on "+str(x[0])+" points: "+str(round((d[x]/n)*100,3))+"%")

main()
