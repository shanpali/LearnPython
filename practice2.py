datalst = ["arun-20","raavi-40","raja-21","somu-5"]
newlst = []
for elem in datalst:
    val = int(elem.split("-")[1])
    if val >= 18 :
        newlst.append(elem.split("-")[0]+ " can vote")
    else :
        newlst.append(elem.split("-")[0]+ " can not vote")

print(newlst)


#comprehension
canvote = [e.split("-")[0] for e in datalst if int(e.split("-")[1])>=18]
print(canvote)


#map
canvote = list(filter(lambda e :  int(e.split("-")[1])>=18 , datalst ))
print(canvote)