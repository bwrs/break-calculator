import random

rooms=int(input("Number of rooms: "))
rounds=int(input("Number of rounds: "))
posquery=int(input("Number of breaking teams: "))
times=int(input("Number of samples (recommended 1000+):"))

def split(t):
    t.sort()
    l=[]
    for i in range(rooms):
        l.append(t[4*i:4*i+4])
    return l

def iteratione(t):
    l=[]
    rs=split(t)
    for i in range(len(rs)):
        random.shuffle(rs[i])
        for ii in range(4):
            l.append(rs[i][ii]+ii)
    return l

def run():
    t=[0 for i in range(rooms*4)]
    for i in range(rounds): t=iteratione(t)
    t.sort()
    k=t[-posquery]
    return (k,t[-posquery:].count(k),t.count(k))

def main():
    d={}
    for i in range(times):
        x=run()
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    return d

def displayd(d):
    print("Sorted by number")
    for k in sorted(list(d)):
        print(str(k[1])+"/"+str(k[2])+" teams on "+str(k[0])+" points"+": "+str((float(d[k])/float(times))*100)+"%")
    print("Sorted by probability")
    for k in sorted([list(x) for x in d.items()],key=lambda x: -x[1]):
        print(str(k[0][1])+"/"+str(k[0][2])+" teams on "+str(k[0][0])+" points: "+str((float(d[k[0]])/float(times))*100)+"%")

d=main()
displayd(d)
