
# define add, subtract, multiply, and divide 

def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

# greeting message
print ("Hello!, Welcome to Iby's simple calculator!")
print (" ")

while True:
    # Collect  user inputs 
    function_input = float(input("What function would you like to use? (1 = add, 2 = subtract, 3 = multiply, 4 = divide) "))
    num1 = float(input("Please type your first number "))
    num2 = float(input("Please type your second number "))
    print ("")

    # define function and answer variables 
    function = ()
    answer = ()
    valid_input = True

    # validate user input 
    if function_input == 1:
        function = "+"
    elif function_input == 2:
        function = "-"
    elif function_input == 3:
        function = "*"
    elif function_input == 4:
        function = "/"

    # conduct calculation based on user input
    if function == "+":
        answer = add(num1,num2)
    elif function == "-":
        answer = subtract(num1,num2)
    elif function == "*":
        answer = multiply(num1,num2)
    elif function == "/":
        answer = divide(num1,num2)
 
 # print calculation and answer
    if valid_input == True:
        print ("Your calculation is:", num1, function, num2)
        print ("Your answer is:", answer )

# Ask if we want to do another calculation
    start_again = input("Would you like to do another calculation? (Yes/No) ")
    print ("")

# End loop
    if start_again == "no":
        break


else: print ("There's a problem")
print ("Thanks, Goodbye!")

        
    
