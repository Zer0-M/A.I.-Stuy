#! /usr/bin/python3
import sys
F=open(sys.argv[1],"r")
boards=F.readlines()
boards=[x.strip("\n") for x in boards]
eob=boards.index(sys.argv[3])
data=boards[eob+1:eob+10]
dat=[]
for line in data:
    each=line.split(",")
    for e in each:
        if e =="_":
            dat.append(0)
        else:
            dat.append(int(e))
Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]\
]
def belongs(i):
    cliqs=[]
    for c in Cliques:
        if i in c:
            cliqs.append(c)
    return cliqs
def possible(i,dat):
    poss=set([1,2,3,4,5,6,7,8,9])
    cliqs=belongs(i)
    for cliq in cliqs:
        for loc in cliq:
            if dat[loc] in poss:
                poss.remove(dat[loc])
    return poss
def toString(dats):
    dats=[str(x) for x in dats]
    st=""
    i=0
    for dat in dats:
        if (i+1)%9==0:
            st+=dat+"\n"
        else:
            st+=dat+","
        i+=1
    return st
def fillobv(dats):
    i=0
    while i<81:
        possset=possible(i,dats)
        if dats[i]==0 and len(possset)==1:
            dats[i]=possset.pop()
        i+=1
    return dats
dat=fillobv(dat)

def solve(dats):
    stateStack=[]
    i=0
    bt=0
    while i<81:
        if dats[i]==0:
            possset=possible(i,dats)
            while len(possset)==0:
                state=stateStack.pop()
                dats=state[0]
                possset=state[1]
                i=state[2]
                bt+=1
            num=possset.pop()
            if len(possset)>0:
                stateStack.append((dats.copy(),possset,i))
            dats[i]=num
            dats=fillobv(dats)
        i+=1
    print(bt)
    return dats
F.close()
F=open(sys.argv[2],"w")
F.write(toString(solve(dat)))
