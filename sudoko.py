F=open("data.txt","r")
data=F.readlines()[1:]
data=[x.strip("\n") for x in data]
print(data)
dat=[]
for line in data:
    each=line.split(",")
    datum=[]
    for e in each:
        if e =="_":
            datum.append(0)
        else:
            datum.append(int(e))
    dat.append(datum)
print(dat)
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
def belongs(r,c):
    cliqs=[]
    index=r*9+c
    for c in Cliques:
        if index in c:
            cliqs.append(c)
    return cliqs
def possible(r,c,dat,tested):
    poss=set([1,2,3,4,5,6,7,8,9])
    cliqs=belongs(r,c)
    for cliq in cliqs:
        for loc in cliq:
            if dat[int(loc/9)][int(loc%9)] in poss:
                poss.remove(dat[int(loc/9)][int(loc%9)])
            elif r*9+c in tested.keys() and tested[r*9+c] in poss:
                poss.remove(tested[r*9+c])
    return poss
def toString(dats):
    st=""
    for r in dats:
        for c in r:
            st+=str(c)+" "
        st+="\n"
    return st
def solve(dats):
    stateStack=[]
    tested={}
    i=0
    while i<9:
        j=0
        while j<9:
            stateStack.append(dats)
            if dats[i][j]==0:
                possset=possible(i,j,dats,tested)
                print(toString(dats))
                print(i,j)
                while  len(possset)==0:
                    print(possset)
                    print(i,j)
                    dats=stateStack.pop()
                    if j==0:
                        i-=1
                        j+=8
                    else:
                        j-=1
                    possset=possible(i,j,dats,tested)
                dats[i][j]=possset.pop()
                if i*9+j not in tested.keys():
                    tested[i*9+j]=[dats[i][j]]
                else:
                    tested[i*9+j].append(dats[i][j])
            j+=1
        i+=1
    return dats
print(solve(dat))
            

