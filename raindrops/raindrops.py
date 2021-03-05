def convert(number = None):
    if number is None:
        print("Enter a valid number")
        return False

    elif number <= 0:
        print("Enter a natural number")
        return False
    
    else:
        if number%3 == 0:
            if number%5 == 0:
                if number%7 == 0:
                    return "PlingPlangPlong"
                else:
                    return "PlingPlang"
            elif number%7 == 0:
                return "PlingPlong"
            else:
                return "Pling"
            
        elif number%5 == 0:
            if number%7 == 0:
                return "PlangPlong"
            else:
                return "Plang"
        elif number%7 == 0:
            return "Plong"
        else:
            return "{}".format(number)


