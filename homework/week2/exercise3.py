def number_adder():
    sum=0
    while True:
        number_to_add = input("Enter a number to add (hit enter if you dont want to add any more numbers): ")
        if number_to_add == "":
            break
        else:
            sum = sum + float (number_to_add)
        print(sum)
number_adder()