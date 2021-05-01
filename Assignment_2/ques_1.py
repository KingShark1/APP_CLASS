given_tuple = (('Red','White','Blue'),('Green','Pink','Purple'),('Orange','Yellow','Lime'))

#to find a tuple in list of tuple
find_tuple = 'White'

for i in range(len(given_tuple)):
    if find_tuple in given_tuple[i]:
        print("tuple exists")