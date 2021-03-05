def is_isogram(string):
    
    string = string.replace(" ", "")
    string = string.replace("-", "")

    lower_str = string.lower()
    my_list = list(lower_str)
    my_set = set(lower_str)

    if len(my_list) == len(my_set):
        return True
    else:
        return False
