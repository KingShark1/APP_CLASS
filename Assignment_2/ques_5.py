given_dict = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}

res = []

for key, value in given_dict.items():
    res.append(key)
    if type(value) == type([]):
        res.extend(value)
    else:
        res.append(value)

print(res)
