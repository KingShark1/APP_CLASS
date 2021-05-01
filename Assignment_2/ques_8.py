def get_words_with_count(file_path:str):
    
    test_file = open(file_path, "r") # 
    res = {}

    for txt in test_file.read().replace("\n", " ").split(" "):
        res[txt.lower()] = (res.get(txt.lower()) or 0) + 1

    test_file.close()
    
    return res

def save_file(content:dict, output_path:str):

    try:
        output_file = open(output_path, 'wt') 
        output_file.write(str(content))
        output_file.close()
    
    except:
        print("Some error occured")

save_file(get_words_with_count("./io.txt"), "output.txt")
