#1a
for number in range (0, 11):
    if (number %3 == 0):
        continue
    else:
        print (number)
#1b
def print_nums():
    for number in range (0,11):
        if number % 3 == 0:
            continue
        print (number)
#1c
max_number = input("What number to do you want to go up to?")
def print_nums(max_number):
    for number in range(0, max_number +1):
        if (number % 3 == 0):
            continue
        print(number)
        
