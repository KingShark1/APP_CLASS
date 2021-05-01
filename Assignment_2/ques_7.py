def count_python(file_path):
    test_file = open(file_path, "r")
    count = 0
    for txt in test_file.read().replace("\n", " ").split(" "):
        if 'python' in txt.lower():
            count += 1

    test_file.close()
    
    return count

print(count_python("./io.txt"))