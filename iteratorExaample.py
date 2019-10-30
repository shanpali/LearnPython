#Forward iterator
namelst = ["bengaluru", "hyd", "delhi"]
for elm in namelst:
    res = elm[0].upper()
    print(res)

print("==============================")
#Reverse iterator
namelst = ["bengaluru", "hyd", "delhi"]
for elm in namelst[::-1]:
    res = elm[0].upper()
    print(res)

print("==============================")
#Reverse iterator
namelst = ["bengaluru", "hyd", "delhi"]
for elm in reversed(namelst):
    res = elm[0].upper()
    print(res)

print("==============================")
#Parallel iterator
a = ['north', "south", "east", 'west']
b = ['delhi','chennai','mumbai','kol']
nlst = list(zip(a,b))

for elm in nlst:
    res = elm
    print(res)

#if two list are different in size, zip will take the lowest one
#if we want the longest iterator we should use "import itertools"

print("==============================")
#Parallel iterator
import itertools
a = ['north', "south", "east", 'west']
b = ['delhi','chennai','mumbai','kol','bangalore']
nlst = list(itertools.zip_longest(a,b))

for elm in nlst:
    res = elm
    print(res)

print("==============================")
#Parallel iterator
import itertools
a = ['north', "south", "east", 'west']
b = ['delhi','chennai','mumbai','kol','bangalore']
nlst = list(itertools.zip_longest(a,b))

for elm1, elm2 in nlst: #using elm1 and elm2
    print(elm1, elm2)

for elm1, elm2 in zip(a,b):
    print(elm1, elm2)

print("==============================")
datlist = ["10-jan","15-dec","31-mar","5-apr"]

#to print months
for elm in datlist:
    res = elm.split("-")[1]
    print(res)

#to print dates
for elm in datlist:
    res = elm.split("-")[0]
    print(res)

nlst = [elm.split("-")[1] for elm in datlist]
print(nlst)