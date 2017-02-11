import random
import decimal as dec
dec.getcontext().prec=4
Dec=dec.Decimal

rooms=int(input("Number of rooms: "))
rounds=int(input("Number of rounds: "))
final=int(input("Number of breaking teams: "))
times=int(input("Number of samples (recommended 10000+):"))

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

def quickplus(d):
    s=set([k[0] for k in d])
    d2={x:Dec(0) for x in s}
    for k in list(d):
        for kk in s:
            if k[0]<kk:
                d2[kk]+=d[k]
            elif k[0]==kk:
                d2[kk]+=(Dec(d[k]*k[1])/Dec(k[2]))
    return d2

def displayd(d,times):
    d2=quickplus(d)
    l=[]
    for k in sorted(list(d2)):
        l.append("Teams with "+str(k)+" points have a "+str(Dec(100*d2[k])/Dec(times))+"% chance of breaking.")
    return l
        
def main(rooms,rounds,final,times):
    d=getdata(rooms,rounds,final,times)
    return displayd(d,times)

print("\n".join(main(rooms,rounds,final,times)))
