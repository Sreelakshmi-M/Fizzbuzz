for Fizzbuzz in range(101):  #range
    if Fizzbuzz%2==0 and Fizzbuzz%7==0:   #check if numb is divisible by 2 and 7
        print("Fizzbuzz")
        continue
    elif Fizzbuzz%2==0:    #check if divisible by 2
        print("Fizz")
        continue
    elif Fizzbuzz%7==0:    #check if divisible by 7
        print("buzz")
        continue
    print(Fizzbuzz)
