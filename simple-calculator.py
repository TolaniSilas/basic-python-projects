
#A Simple Calculator
#This Program Performs Arithmetic Operation Between 2 Operands

print("Welcome, Let's Calculate!")


while True:
    
    print("""
    To Perform Arithmetic Operations;
    1 - Additon
    2 - Subtraction
    3 - Multiplication
    4- Division
    Off- To off the calculator.
    """)
    print("Hint: Enter numbers from range 1 to 4 only.\n")
    
    try:
        user_input = input("Enter Number For Choice Of Arithmetric Operation: ")
        
        if user_input.title() == "Off":
            print("Calculator is off! Thanks for using!")
            print("Run the code to \"ON\" the calculator if you still want to calculate!")
            break
    
    
        if 0<int(user_input)<5:
            print("Enter The 2 Operands: ")
    
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
    
            if int(user_input) == 1:
                def add(num1, num2):
                    """This function add two numbers."""
                    
                    return num1 + num2
                print("The Final Result is =",add(num1,num2))

            elif int(user_input) == 2:
                def subtract(num1, num2):
                    """This function subtract two numbers."""
                    
                    return num1 - num2
                print("The Final Result is =",subtract(num1,num2))
        
            elif int(user_input) == 3:
                def multiply(num1, num2):
                    """This function multiply two numbers."""
                    return num1 * num2
                print("The Final Result is =",multiply(num1,num2))
        
            elif int(user_input) == 4:
                def divide(num1, num2):
                    """This function divide two numbers."""
                    
                    # Raises an error if the first number is divided by zero, else return the result.
                    if num2 == 0:
                        return "Error! Cannot Divide By Zero!"
                    
                    else:
                        return num1 / num2
                    
                print(divide(num1,num2))
    
    # raise ValueError if user_input prompt accepts any other input apart from those listed in the instruction menu.            
    except ValueError:
        print("Oops! Read the help instruction!")
