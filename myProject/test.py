import os
import sys


os.system("cls")

name = input("Enter your name to continue: ")

countName = len(name)

if countName > 1:
    os.system("cls")

    print("Welcome to Calculator " + name + "!")
    print("\n\nOperations")
    print("\nAddition       [1]     Subtraction [2]")
    print("\nMultiplication [3]     Division    [4]")

    operation = input("\n\n\n\nSelect your desired operation to use: ")

    # Addition
    if operation == "1":
        os.system("cls")
        print("Addition")
        num1 = input("\n\nEnter your first number: ")
        num2 = input("\n\nEnter your second number: ")

        intNum1 = int(num1)
        intNum2 = int(num2)

        answer = intNum1 + intNum2

        print("\n\nAnswer is: " + str(answer))
