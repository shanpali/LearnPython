#Question : datalst = ["10-20","30-40","50-60","70-80"]
# output shoudl be  = [2, 4, 6, 8]


datalst = ["10-20","30-40","50-60","70-80"]
newlst = []
for elem in datalst:
    val = elem.split("-")[1][0]
    newlst.append(int(val))

print(newlst)

#comprehension
newlst = [int(elem.split("-")[1][0]) for elem in datalst]
print(newlst)


#map
newlst = list(map(lambda elem :  int(elem.split("-")[1][0]) , datalst ))
print(newlst)

