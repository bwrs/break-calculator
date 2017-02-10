import random

rooms=int(input("Number of rooms: "))
rounds=int(input("Number of rounds: "))
posquery=int(input("Number of breaking teams: "))
times=int(input("Number of samples (recommended 10000+):"))

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

def quickify(d):
    d2={}
    for i in list(d):
        if i[0] in d2:
            d2[i[0]]+=d[i]
        else:
            d2[i[0]]=d[i]
    return d2

def quickplus(d):
    s=set([k[0] for k in d])
    d2={x:0 for x in s}
    for k in list(d):
        for kk in s:
            if k[0]<kk:
                d2[kk]+=d[k]
            elif k[0]==kk:
                d2[kk]+=d[k]*(k[1]/float(k[2]))
    return d2

def displayd(d):
    print("Quick output")
    d2=quickplus(d)
    for k in sorted(list(d2)):
        print("Teams with "+str(k)+" points have a "+str(100*(d2[k]/float(times)))+"% chance of breaking.")
    print ("Sorted by compound (cumulatively)")
    t=0.0
    for k in sorted(list(d), key=lambda x: 2*x[0]+(float(x[1])/x[2])):
        t+=(float(d[k])/float(times))*100
        print(str(k[1])+"/"+str(k[2])+" teams on "+str(k[0])+" points"+": "+str(t)+"%; increase of "+str((float(d[k])/float(times))*100)+"%")
    print("Sorted by probability")
    for k in sorted([list(x) for x in d.items()],key=lambda x: -x[1]):
        print(str(k[0][1])+"/"+str(k[0][2])+" teams on "+str(k[0][0])+" points: "+str((float(d[k[0]])/float(times))*100)+"%")

d=main()
displayd(d)
