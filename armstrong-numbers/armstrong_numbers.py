def is_armstrong_number(number):
    numTostr = str(number)
    my_list = list(numTostr)
    my_numbers = []
    for i in my_list:
        each = int(i)
        my_numbers.append(each)
     
    print(my_numbers)
    my_len = len(my_numbers)
    print(my_len) #3

    print(my_numbers[0]) #1
    cnt = my_numbers[0]**my_len #1**3
    for i in range(0, my_len):
        if i ==0:
            pass
        else:
            cnt += my_numbers[i]**my_len
    
    if cnt == number:
        print(cnt)
        return True
    if cnt != number:
        print(cnt)
        return False


is_armstrong_number(153)
