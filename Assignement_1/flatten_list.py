import numpy as np
def flatten_list(a):
    nparray = np.array(a)
    return np.ndarray.flatten(nparray)

a =[[1,2,3],[1,2,3],[4,5,6]]
print(flatten_list(a))
