import random
from Tkinter import *

rooms=int(input("enter #rooms: "))
rounds=int(input("enter #rounds: "))
posquery=int(input("enter #people in final: "))
times=int(input("enter #times to run:"))

def stringify(d):
    s=''
    for k in sorted(list(d)):
        s+=str(k)+": "+str(d[k])+"\n"

class App:

    def __init__(self,master):
        self.master=master

        self.roomslabel=Label(master,text="Number of rooms:")
        self.roomslabel.grid(row=0,column=0)
        self.roomsentry=Entry(master)
        self.roomsentry.grid(row=0,column=1)

        self.roundslabel=Label(master,text="Number of rounds:")
        self.roundslabel.grid(row=1,column=0)
        self.roundsentry=Entry(master)
        self.roundsentry.grid(row=1,column=1)

        self.poslabel=Label(master,text="Number of final places:")
        self.poslabel.grid(row=2,column=0)
        self.posentry=Entry(master)
        self.posentry.grid(row=2,column=1)

        self.runslabel=Label(master,text="Number of runs:")
        self.runslabel.grid(row=3,column=0)
        self.runsentry=Entry(master)
        self.runsentry.grid(row=3,column=1)

        self.v=StringVar()
        self.outlabel=Label(master,textvariable=self.v)
        self.outlabel.grid(row=0,rowspan=3,column=2)

        self.bigbutton=Button(master,text="Run",command=self.majulah)
        self.bigbutton.grid(row=3,column=2)

    def split(self,t,rooms):
        t.sort()
        l=[]
        for i in range(rooms):
            l.append(t[4*i:4*i+4])
        return l

    def iteratione(self,t,rooms):
        l=[]
        rs=self.split(t,rooms)
        for i in range(len(rs)):
            random.shuffle(rs[i])
            for ii in range(4):
                l.append(rs[i][ii]+ii)
        return l

    def run(self,rooms,rounds,posquery):
        t=[0 for i in range(rooms*4)]
        for i in range(rounds): t=self.iteratione(t,rooms)
        t.sort()
        return t[-posquery]

    def main(self,rooms,rounds,posquery,times):
        d={}
        for i in range(times):
            x=self.run(rooms,rounds,posquery)
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        return d

    def majulah(self):
        rooms=int(self.roomsentry.get())
        rounds=int(self.roundsentry.get())
        pos=int(self.posentry.get())
        runs=int(self.runsentry.get())
        update=100
        d={}
        for i in range(int(runs)):
            if 
                    



d=main()
for k in d:
    print(str(k)+": "+str(d[k]))
