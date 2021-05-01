original_tuple = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

def remove_duplicates(test_tuple):
    '''
        Iterates through test_tuple returning only unique values
    '''
    res = []
    for ls in test_tuple:
        if(ls not in res):
            res.append(ls)

    return tuple(res)


print(remove_duplicates(original_tuple))