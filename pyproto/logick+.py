import random

rooms=int(input("enter #rooms: "))
rounds=int(input("enter #rounds: "))
posquery=int(input("enter #teams in final: "))
times=int(input("enter #times to run:"))

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
    for k in sorted(list(d)):
        print(str(k[0])+" points; "+str(k[1])+"/"+str(k[2])+": "+str(d[k]))

d=main()
displayd(d)
