tuple_A = (7, 2)
tuple_B = (7, 8) 

def permute_tuple(tuple1, tuple2):
    permuted_list = []
    for i in tuple1:
        for j in tuple2:
            permuted_list.append(tuple((i, j)))
    
    for i in tuple2:
        for j in tuple1:
            permuted_list.append(tuple((i, j)))
    
    return permuted_list

print(permute_tuple(tuple_A, tuple_B))