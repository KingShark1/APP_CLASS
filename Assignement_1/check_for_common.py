#takes two string and returns bool if atleast one element is common
def check_common(a, b):
    for i in a:
        if(i in b):
            return True
    
        

a = [1,2,3]
b = [4,5,6]
c = [2,3,4]

print(check_common(a,b))
print(check_common(a,c))
