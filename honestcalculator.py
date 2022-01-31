# Honest calculator project from https://hyperskill.org.

from ast import Index
import messages
import functions
import variables

while variables.ok1 == False and variables.ok2 == False:
    variables.ok5 = False
    result = 0
    print(messages.msg_0)  # Prints the initial message
    operation = input()
    parts = operation.split() # Splits the input into three: x, y and operator.
    try:
        x = parts[0]
        oper = parts[1]
        y = parts[2]  
        if x == "M":  # Checks if the user wants to add number to memory.
            x = variables.memory
        if y == "M":
            y = variables.memory
        try:
            x = float(x)  
            y = float(y)
            if functions.is_int(x):  # Checks if the number's fractional part is zero.
                x = int(x)  # If that is the case, it turns it into an integer.
            if functions.is_int(y):
                y = int(y)
            if oper in variables.valid_operations:
                functions.check(x, y, oper)
                try:
                    if oper == "+":
                        result = x + y
                    elif oper == "-":
                        result = x - y
                    elif oper == "*":
                        result = x * y
                    elif oper == "/":
                        result = x / y    
                    print(float(result))
                    if variables.ok2 == False:
                        print(messages.msg_4)  
                        first_answer = input()
                        if first_answer == "y":
                            if functions.is_int(result):
                                result = int(result)
                            if functions.is_one_digit(result):  # Checks if the result is only one digit
                                variables.ok4 = False
                                while variables.ok4 == False: # Loops through messages until user gives up/in. 
                                    msg_index = 10 
                                    print(messages.message_list[msg_index - 10])
                                    third_answer = input()
                                    while third_answer == "y" and variables.ok5 == False:
                                        if msg_index < 12:
                                            msg_index += 1
                                        print(messages.message_list[msg_index - 10])
                                        third_answer = input()
                                        if third_answer == "y" and msg_index == 12:
                                            variables.memory = result
                                            variables.ok5 = True 
                                    variables.ok4 = True   
                            else: 
                                variables.memory = result
                        print(messages.msg_5)
                        second_answer = input()
                        if second_answer == "n":
                            variables.ok2 = True
                except ZeroDivisionError:
                    print(messages.msg_3) 
            else:
                print(messages.msg_2)
        except ValueError:
            print(messages.msg_1)
    except IndexError:
            print("Invalid input")