def prime_number(value):
    if  value != 1:
        for f in range(2, value+1):
            print("-----------", f, "------------") 
            if value % f != 0:
                print("no")
                return False
    else: 
        print("no")
        return False
    print("yes")
    return True

prime_number(3)
    

def factors(value):
    integer_list = []
    for i in range(2, value+1):
        integer_list.append(i)
    print("integer_list:", integer_list)  #2,3,4,5

    prime_numbers = []

    for num in integer_list: #2
        print(num)
        if prime_number(num):
            prime_numbers.append(num)
            print(prime_number(num))
        else:
            print(prime_number(num))


    print("prime numbers:", prime_numbers)
    return prime_numbers


# factors(5)