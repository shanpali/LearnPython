# phone book
# lookup table
# non sequest
# O(1)


forex = {"yen":24,"euro":80,"dollar":71,"ster":120}

if "ringet" in forex.keys():
    curr = forex["ringet"]
    print("yes we deal with ringet : " + str(curr))

if "yen" in forex.keys():
    curr = forex["yen"]
    print("yes we deal with yen : " + str(curr))



print("==============================")

stab = {"blr": [10,20,30,40],
        "mum": [10,5,2,7],
        "hyd": [10,5,6,2],
        "tvn": [50,30,10]}
#part 1
for elem in stab:
    print(elem)
    print(sum(stab.get(elem)))
#part 2
for key,value in stab.items():
    print(key,sum(value))
