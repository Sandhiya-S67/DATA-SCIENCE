print("Welcome to the application!")
num = 1
while(num):
    a = int(input("Enter the value of the first number:"))
    b = int(input("Enter the value of the second number:"))
    print("Calculator Operations:")
    choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
    if(choice == 1):
        result = a+b
        print(f"Sum of {a} and {b} is {result}")
    elif(choice == 2):
        result = a-b
        print(f"Subtraction of {b} from {a} is {result}")
    elif(choice == 3):
        result = a*b
        print(f"Product of {a} and {b} is {result}")
    elif(choice == 4):
        result = a // b
        print(f"Division of {a} by {b} is {result}")
    else:
        print("Invalid Choice!")
    num = int(input("If you want to continue enter any number other than zero:"))
print("Thank you!")
