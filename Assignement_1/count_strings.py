#takes a string argument and returns int according to conditions
#given in question

def count_string(s):
    num = 0
    for i in range(len(s)):
        if((len(s[i]) > 2) and (s[i][0]==s[i][-1])):
            num+=1
    return num

string = ['abc', 'xyz', 'aba', '1221']
print(count_string(string))