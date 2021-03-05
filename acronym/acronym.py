def abbreviate(words):
    words = words.upper()
    words = words.replace("-", " ")
    words = words.replace("_", " ")
    my_list = words.split()
    # print(my_list)
    my_dict = []
    for i in my_list:
        sec_list = list(i) 
        # print(sec_list)
        my_dict.append(sec_list[0])
    # print(my_dict)
    result = ''.join(my_dict)
    # print(result)
    return result
