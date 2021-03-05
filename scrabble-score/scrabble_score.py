def score(word):
    letter = {1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
              2 : ["D", "G"],
              3 : ["B", "C", "M", "P"],
              4 : ["F", "H", "V", "W", "Y"],
              5 : ["K"],
              8 : ["J", "X"],
              10 : ["Q", "Z"]
    }
    print(word)
    my_word = word.upper()
    my_list = list(my_word)
    print(my_list)

    cnt = 0
    for item in my_list:
        if item in letter[1]:
            cnt += 1
        elif item in letter[2]:
            cnt += 2
        elif item in letter[3]:
            cnt += 3
        elif item in letter[4]:
            cnt += 4
        elif item in letter[5]:
            cnt += 5
        elif item in letter[8]:
            cnt += 8
        elif item in letter[10]:
            cnt += 10
        
    return cnt


score("quirky")
