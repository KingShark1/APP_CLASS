from remove_duplicates import rem_duplicates

def count_freq_in_list(a):
    new_set = rem_duplicates(a)
    freq_of_new_set = []
    for i in new_set:
        count=0
        for j in a:
            if(i==j):
                count+=1
        
        freq_of_new_set.append(count)
        
    
    count_in_dict = dict(zip(new_set, freq_of_new_set))
    return count_in_dict

my_list = ["Paras", "Jain", "Cyware", "Manas", "Paras", "1", "1", "1"]
print(count_freq_in_list(my_list))
