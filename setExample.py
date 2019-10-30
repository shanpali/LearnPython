studs = [1,2,3,4,5,6,7,8,9,10]
chess = [5,3,9,1]
carrom = [4,5,10,8]
pinnball = [1,8,4,3,5]


#student who plays all the games
a = set(studs)
b = set(chess)
c = set(carrom)
d = set(pinnball)
res = b&c&d
print(res)




#Student who doesn't play any game

res = set(studs) - b|c|d
print(res)