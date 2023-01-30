print("X",end="|")
for i in range (1,10):
    print("{0:<2}".format(i),end="|")

print("")

for i in range(1,10):
    print(i,end="|")
    for j in range(1,10):
        result = i * j
        print("{0:<2}".format(result), end="|")
    
    print("")