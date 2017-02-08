from operator import add
from collections import Counter,defaultdict
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
    m = [br[-f:][0] for br in s]
    e = [(m[i],s[i][-f:].count(m[i]),s[i].count(m[i])) for i in range(len(m))]
    d = list(Counter(e).items())
    o = defaultdict(list)
    for y in d:
        o[y[0][0]].append(y)
    u = [[(y[0][0],y[0][1]*y[1],y[0][2]*y[1]) for y in x] for x in list(o.values())]
    p = [[x[0][0]]+[sum(y) for y in list(zip(*x))[-2:]] for x in u]
    c = [[x[0],round((x[1]/x[2])*100*x[2]/sum([y[2] for y in p]),1)] for x in p]
    d = [round(100*x[2]/sum([y[2] for y in p]),1) for x in p]
    i = [[c[x][0],sum([y for y in d[0:x]])+c[x][1]] for x in range(len(c))]
    for b in i:
        print("Teams on "+str(b[0])+" points have a "+str(b[1])+"% chance of breaking.")

main()

