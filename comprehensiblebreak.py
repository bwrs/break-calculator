from operator import add
from random import shuffle
from collections import Counter

def p():
    r = list(range(4))
    shuffle(r)
    return r

def process(tab,rounds):
    for i in range(rounds):
        tab = sorted(map(add,tab,[x for y in [p() for i in range(int(len(tab)/4))] for x in y]))#processes tab and adds new points
    return tab

def main():
    teams = int(input("Number of rooms: ")) * 4
    rounds = int(input("Number of rounds: "))
    final = int(input("Number of breaking teams: "))
    iterations = int(input("Number of iterations (recommended 1000+): "))
    sample = [process([0 for i in range(teams)],rounds) for i in range(iterations)]
    minimum = [list(set(breaking[-final:]))[0] for breaking in sample]
    prob = [(minimum[i],sample[i][-final:].count(minimum[i]),sample[i].count(minimum[i])) for i in range(len(minimum))]
    probabilities = dict(Counter(prob))
    for break_requirement in sorted(d.keys(), key = lambda x: -d[x]):
        print(str(probabilities[1])+"/"+str(probabilities[2])+" on "+str(probabilities[0])+" points: "+str(round((probabilities[break_requirement]/iterations)*100,3))+"%")

main()
