#Spectre terminal-based basic calculator

import os
import time
from colors import Colors

#introduction meassage

intro = f'''
     _______________________________
    |                               |
    | 🤖 {Colors.CYAN}SPECTRE CLI CALCULATOR{Colors.RESET} 🤖  |
    |______________________________ |

    |SYSTEM|
    Status : 🟡 Ready
    Version : 1.0.0

'''
operations = '''
    |Operations|
    
        [1] Addition 
        [2] Subtraction
        [3] Multiplication
        [4] Division 
        [5] Power 
        [6] Modulus
        [7] History
        [0] Exit ❌
'''

print(intro)

#getting operation command and validating input
def getOperation():
    while True:
        try:
            operation = input("Select Operations(1-7 0r 0 to exit)> ")
            operation = int(operation)
            if operation < 0 or operation > 7:
                print("404 | Error⚠: Operation can only be between 0 and 7.")
            else:
                return operation
        except ValueError:
            print("404 | Error⚠: Operation must be a digit.")

def getNum():
    while True:
        try:
            operand = input("Enter a Number > ")
            operand = int(operand)
            return operand
        except ValueError:
            print(f"404 | Error⚠ :{operand} is not a valid digit.")

def calculate(operation):
    FirstNum = getNum()
    SecondNum = getNum()
    if operation == 1:
        output = f"{FirstNum} + {SecondNum}  = {FirstNum + SecondNum}"
    elif operation == 2:
        output = f"{FirstNum} - {SecondNum}  = {FirstNum - SecondNum}"
    elif operation == 3:
        output = f"{FirstNum} * {SecondNum}  = {FirstNum * SecondNum}"
    elif operation == 4:
       try:
           output = f"{FirstNum} / {SecondNum}  = {FirstNum / SecondNum}"
       except ZeroDivisionError:
           output = "404 Error"
           print(f"{Colors.RED}<Math Error!! Can't find the modulus.{Colors.RESET}>")
    elif operation == 5:
       output = f"{FirstNum} ^ {SecondNum}  = {FirstNum ** SecondNum}"
    elif operation == 6:
        try:
            output = f"{FirstNum} % {SecondNum}  = {FirstNum % SecondNum}"
        except ZeroDivisionError:
            output = "404 Error"
            print(f"{Colors.RED}<Math Error!! Can't find the modulus.{Colors.RESET}>")

    with open("history.txt","w",encoding="utf-8") as file:
        file.write(output)
    return output

def main():
   while True:
       print(operations)
       operation = getOperation()
       if operation in range(1,7):
           output = calculate(operation)
           print("Thinking...")
           time.sleep(1)
           print("Compiling result")
           time.sleep(1)
           print(output)
       elif operation == 7:
           try:
               with open("history.txt","w",encoding="utf-8") as file:
                   file.write(output)
           except FileNotFoundError:
               print("Opps!! There seem to be a problem at our end.")
       elif operation == 0:
           break


if __name__ == "__main__":
    main()
