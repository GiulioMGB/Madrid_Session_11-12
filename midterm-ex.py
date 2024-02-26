def m6():
    """
    A function that returns a multiple of 6

    :return: the multiple of 6 number entered by the user
    """
    while True:
        try:
            #first we need to read the number
            number = input("Please give me a multiple of 6 number ")
            number = int(number)
        except ValueError:
            # if the number is not valid, print an error and retry
            print("This is not a number please retry ")
            continue
        #check if the number is a multiple of 6
        if number % 6 == 0:
            return number
        #print an error and try again
        print("This number is not a multiple of 6 please retry ")

print("a multiple of 6 is", m6())

