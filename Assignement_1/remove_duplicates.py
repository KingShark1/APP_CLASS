#program to remove duplicates from a list
#only does for string
def rem_duplicates(string):
    new_list = set(string)
    return new_list

print(rem_duplicates(
['123',
'345',
'123',
'567',
'345'])
)

