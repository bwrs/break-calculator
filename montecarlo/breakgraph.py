import random
import matplotlib.pyplot as plt
import decimal as dec
dec.getcontext().prec=4
Dec=dec.Decimal

try:
    input=raw_input
    print("Running Python 2")
except:
    print("Running Python 3")

rooms=int(input("Number of rooms: "))
rounds=int(input("Number of rounds: "))
final=int(input("Number of breaking teams: "))
times=int(input("Number of samples (recommended 10000+):"))
graph=str(input("Enter chosen graph: ")).strip()
params=str(input("Enter extra parameters: "))

def split(t,rooms):
    t.sort()
    l=[]
    for i in range(rooms):
        l.append(t[4*i:4*i+4])
    return l

def iteratione(t,rooms):
    l=[]
    rs=split(t,rooms)
    for i in range(len(rs)):
        random.shuffle(rs[i])
        for ii in range(4):
            l.append(rs[i][ii]+ii)
    return l

def run(rooms,rounds,posquery):
    t=[0 for i in range(rooms*4)]
    for i in range(rounds): t=iteratione(t,rooms)
    t.sort()
    k=t[-posquery]
    return (k,t[-posquery:].count(k),t.count(k))

def getdata(rooms,rounds,final,times):
    d={}
    for i in range(times):
        x=run(rooms,rounds,final)
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    return d

def dataconvert(d):
    d2={k[0]+k[1]/float(k[2]):0 for k in d}
    for k in d:
        d2[k[0]+k[1]/float(k[2])]+=d[k]
    return d2

def draw(d,graph,params):
    ks=list(d)
    ks.sort()
    ds=[d[k] for k in ks]
    #plt.fill_between(ks,ds)
    #plt.step(ks,ds)
    if params!="":
        if params[0]!=",":
            params=","+params
    exec("plt."+graph+"(ks,ds"+params+")")
    plt.show()

draw(dataconvert(getdata(rooms,rounds,final,times)),graph,params)
