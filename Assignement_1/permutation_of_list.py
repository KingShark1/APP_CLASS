from itertools import permutations

def permute(a):
    list1 =list(permutations(a))
    print(list1)

a = ['a','b','c']
permute(a)
