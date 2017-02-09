from operator import add
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
    rooms = int(input("Number of rooms: "))
    rounds = int(input("Number of rounds: "))
    final = int(input("Number of breaking teams: "))
    iterate = int(input("Number of iterations (recommended 1000+): "))
    sample = [process([[0]*rooms*4][0],rounds,rooms) for i in range(iterate)]
    b = [x[-final:] for x in sample]
    points = [[b[i][0],b[i].count(b[i][0]),sample[i].count(b[i][0])] for i in range(iterate)]
    split = {}
    for x in points:
        split.setdefault(x[0], []).append(x)
    nag = [[x[0][0],sum(x[1]),sum(x[2])] for x in [list(zip(*split[x])) for x in split.keys()]]
    agd = [[nag[i][0],sum([y[2] for y in nag[:i]]),sum([y[2] for y in nag])] for i in range(len(nag))]
    prob = [[nag[i][0],100*nag[i][1]/sum(x[2] for x in nag)+agd[i][1]/agd[i][2]] for i in range(len(nag))]
    for point in prob:
        print("Teams on",str(point[0]),"points have a",str(point[1])+"% chance of breaking.")

main()
