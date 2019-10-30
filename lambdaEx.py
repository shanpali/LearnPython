print("==============================")

f1 = lambda x : x*x # getting square
f2 = lambda x,y : x+y # getting some
f3 = lambda x,y : x if x>y else y # getting max


print(f1(5))
print(f2(5,6))
print(f3(5,2))


#Application of lambda
#custom-sort
studlst = ["ravi-40", "john-75","arun-60","hari-80","manu-76"]
studlst.sort(key = lambda x : int(x.split("-")[1]))
print("\n".join(studlst))