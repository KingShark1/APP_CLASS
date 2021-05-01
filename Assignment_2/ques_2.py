#the given tuple in ques 2
given_tuple = [(1,2),(2,3),(3,4)]
sum_of_tuple = []

#iterates through the the list with each tuple
for tuple in given_tuple:
    #adds the sum of tuple list to the end of "sum_of_tuple" list
    sum_of_tuple.append(tuple[0] + tuple[1])

#prints the updated "sum_of_tuple" list
print(sum_of_tuple)