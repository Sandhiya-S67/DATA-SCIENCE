import calendar
print("Welcome to the calendar application!")
num = 1
while(num):
    print("Enter your choice from the below:")
    choice = int(input("1.To display all the months in a year\n2.To display a particular month in a year\n"))
    if(choice == 1):
        yy = int(input("Enter the year to be displayed:"))
        print(calendar.calendar(yy))
    elif(choice == 2):
        yy = int(input("Enter the year to be displayed:"))
        mm = int(input("Enter the month to be displayed:"))
        print(calendar.month(yy , mm))
    else:
        print("Invalid Choice!")
    num = int(input("If you want to continue enter any number other than zero:"))
print("Thank you!")
