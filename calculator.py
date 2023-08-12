def Addition(user_num1, user_num2): # add two numbers
    addResult= user_num1 + user_num2
    return addResult
def Subtraction(user_num1, user_num2): # subtract two numbers
    diffResult= user_num1 - user_num2
    return diffResult
def Product(user_num1, user_num2): # multiply two numbers
    prodResult= user_num1 * user_num2
    return prodResult
def Quotient(user_num1, user_num2): # divide two numbers
    if user_num2 != 0: # zero division error
        divResult= user_num1 / user_num2
        return divResult
    else:
        print("Cannot divide a number by 0")
def FloorDivision(user_num1, user_num2): # floor division of two numbers
    if user_num2 != 0: # zero division error
        floor_divResult= user_num1 // user_num2
        return floor_divResult
    else:
        print("Cannot divide a number by 0")
def SquareNumber(user_num1): # square a number
    squareResult= (user_num1 ** 2)
    return squareResult
def CubeNumber(user_num1): # cube of number
    cubeResult= (user_num1 ** 3)
    return cubeResult
def SquareRoot(user_num1): # square root of number
    sqrtResult= user_num1 ** (1/2)
    return sqrtResult
def CubeRoot(user_num1): # cube root of number
    cube_rootResult= user_num1 ** (1/3)
    return cube_rootResult
def main():
    calculationResult= None
    userChoice= int(input("Press 1 to use Calculator: "))
    while(userChoice == 1): # loop for repition of calculations
        userChoice= input("Press b for binary operand calculations OR u for unary operand calculations: ")
        if userChoice not in ['b', 'u', 'B', 'U']: # input error validation
            print("Invalid Input!")
            continue # back to loop
        if userChoice == 'b' or userChoice == 'B':
            try: # number error validation
                user_num1= float(input("Input first number: "))
                user_num2= float(input("Input second number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue # back to loop 
            print("+ : Addition\n- : Subtraction\n* : Product\n/ : Quotient\n// : Floor Division\n")
            userOperation= input("Enter an operation: ")
            if userOperation not in ['+', '-', '*', '/', '//']: # operation error validation
                print("Please enter a valid operation.")
                continue # back to loop
            if userOperation == '+':
                calculationResult= Addition(user_num1, user_num2)
            elif userOperation == '-':
                calculationResult= Subtraction(user_num1, user_num2)
            elif userOperation == '*':
                calculationResult= Product(user_num1, user_num2)
            elif userOperation == '/':
                calculationResult= Quotient(user_num1, user_num2)
            elif userOperation == '//':
                calculationResult= FloorDivision(user_num1, user_num2)
        elif userChoice == 'u' or userChoice == 'U':
            print("**2 : Square\n**3 : Cube\ns : Square Root\nc : Cube Root\n")
            userOperation= input("Enter an operation: ")
            if userOperation not in ['**2', '**3', 's', 'c']: # operation error validation
                print("Please enter a valid operation.")
                continue # back to loop
            if userOperation == '**2':
                user_num1= int(input("Input number: "))
                calculationResult= SquareNumber(user_num1)
            elif userOperation == '**3':
                user_num1= int(input("Input number: "))
                calculationResult= CubeNumber(user_num1)
            elif userOperation == 's':
                user_num1= int(input("Input number: "))
                calculationResult= SquareRoot(user_num1)
            elif userOperation == 'c':
                user_num1= int(input("Input number: "))
                calculationResult= CubeRoot(user_num1)
        print("Answer:", calculationResult)
        userChoice= int(input("Press 1 to use calculator again: "))
        if userChoice != 1: 
            print("ABORT CALCULATOR")  
if __name__ == "__main__":
    main()