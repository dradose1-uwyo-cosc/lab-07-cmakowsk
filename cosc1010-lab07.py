# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/3/24
# Lab 07
# Lab Section: 15
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
while True:
    Upper_input = input("Give upper bound here:")

    if Upper_input.isdigit() and int(Upper_input) > 0:
        upper_bound = int(Upper_input)
        factorial = 1

        for number in range (1, upper_bound + 1):
        # the upper_bound +1 is because you gotta remember python excludes the last number in a range
        # for example range 1,4 is actually gonna only do numbers 1,2, and 3
            factorial *= number
        #multiply the original number times however many times until number isn't in range

        print(f"The result of the factorial based on the given bound is {factorial}")
        break
    else:
        print("Please give a positive integer")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
num_sum = 0
while True:
    integer_val = input("Type Number Here:")
    if integer_val.lower() == "exit":
        break
    if integer_val.lstrip('-').isdigit():
        num_sum += int(integer_val)
    else:
        print("Please give an integer")
    

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

while True:
    Calc_str = input("Enter Equation here:")
    operators = ['+', '-', '*', '/', '%']
    Calc_str = Calc_str.replace(" ", "")
    operator = None
    for op in operators:
        if op in Calc_str:
            operator = op
            break
    if operator == None:
        print("Error: retype equation")
        answer = "Error"
    split_str = Calc_str.split(operator)
    if split_str[0].isnumeric() and split_str[1].isnumeric():
        number1 = int(split_str[0])
        number2 = int(split_str[1])
    if operator == '+':
        answer = number1 + number2
    if operator == '-':
        answer = number1 - number2
    if operator == '*':
        answer = number1 * number2
    if operator == '/':
        answer = number1/number2
    if operator == '%':
        answer = number1 % number2
    if Calc_str.lower() == 'exit':
        break
    print(f"Your Answer is: {answer}")


        