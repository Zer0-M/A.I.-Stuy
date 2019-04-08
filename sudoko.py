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
