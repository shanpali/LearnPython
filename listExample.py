#list is mutable
#inplace vs outPlace
#Lambda s - sort


# Basic operations of list :
# define empty list
# define a list
# length
# search for 40
# append
# delete
# sort
# reverse


# inPlace and OutPlace

#inplace
from collections import OrderedDict

a = [10,20,30]
print(id(a))
a.append(40)
print(id(a)) # same id as first one
a.pop(0)
print(id(a))# same id as first one
a.sort()
print(id(a))# same id as first one
print(a)

#outPlace
a = [10,20,30]
print(id(a))
a= a+[50]
print(id(a)) # different id then first one
print(a)



print("==============================")

alst = [10,20,30,40]
blst = alst
alst[0:3] = ["*"]*4

if alst == blst :
    print("yes")
else:
    print("no")


print("==============================")
alst = [10,20,30]
blst = ['a','b','c']
clst = []
for i,j in zip(alst, blst):
    clst.append(i)
    clst.append(j)

print(clst)

print("=======================================")
print("Removing duplicates from list by keeping the order of the list")

l=[1,1,2,3,3,5,6,6,8,8,9,9,10,10]
print("Before removing")
print(l)
l = list(OrderedDict(zip(l, l)).values())
print("After removing")
print(l)
