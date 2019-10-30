msg = "today is a sunny day"
a = msg.split(" ")
a[0] = a[0].upper()
a[-1] = a[-1].upper()
res = " ".join(a)

print(res)


lst = [10,20,30,40,50]
it = iter(lst)

while(next(it)):
 print(*it) #print whole data

# Equal distribution
lst = [10,20,30,40,50]
it = iter(lst)
a,b,c,d,e = it
print(a)
print(b)
print(c)
print(d)
print(e)

#Unequal distribution
lst = [10,20,30,40,50]
it = iter(lst)
*a,b,c = it  #Put a star in front of any reference

print(a) # 10,20,30
print(b) #40
print(c) #50


lst = [10,20,30,40,50]
it = iter(lst)
a,b,c,d,e = it


