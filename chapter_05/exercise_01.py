#write a program which repeatedly reads number until the user enters "done". Once "done" is entered,print out
#the total, count, and average of the numbers. If the user enters anything other than a number, detect their
#mistake using try and except and print an error message and skip to the next number.
value = 0 
iteration = 0

while True:
   
    input_value = input("Enter a number: ")
    
    if input_value == 'done':
        print(value, iteration, value/iteration)
        break
    try:
        value += float(input_value)
        iteration += 1
    except:
        print("invalid input")
    



   
