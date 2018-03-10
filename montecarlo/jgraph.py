from operator import add
from numpy.random import shuffle
from collections import Counter
import matplotlib.pyplot as plt
from itertools import chain

def gen(shufflee = list(range(4))):
    shuffle(shufflee)
    return shufflee

def process(tab,rounds,rm):
    for i in range(rounds):
        tab = sorted(list(map(add,tab,list(sum([gen() for i in range(rm)],[])))))
    return sorted(tab)

def opp(rooms,rounds,final,iterate):
    sample = [process([[0]*rooms*4][0],rounds,rooms) for i in range(iterate)]
    b = [x[-final:] for x in sample]
    points = [(b[i][0],b[i].count(b[i][0]),sample[i].count(b[i][0])) for i in range(iterate)]
    return Counter(points)

def main():
    rooms = [64]
    rounds = [16]
    final = [128]
    sample = [sorted(list(dict(opp(a,b,c,10000)).items()),key=lambda x: x[1]) for a in rooms for b in rounds for c in final]
    for x in sample[:5]:
        plt.plot(*list(zip(*[[y[0][0]+y[0][1]/y[0][2],y[1]] for y in x][::-1])))
        plt.show()
    
main()
