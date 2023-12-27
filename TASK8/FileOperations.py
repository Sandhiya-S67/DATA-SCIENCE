import os

print("Welcome to the application!")
num = 1
while(num):
    print("The list of file Operations:")
    choice = int(input("1.Creation\n2.Insertion\n3.Updation\n4.Deletion\n"))
    file = input("Enter the name of the file to be created:")
    if(choice == 1):
        content = input("Enter the text to be inserted:")
        with open(file , 'w') as file1:
            file1.write(content)
    elif(choice == 2):
        content = input("Enter the text to be inserted:")
        with open(file , 'a') as file1:
            file1.write(content)
    elif(choice == 3):
        content = input("Enter the text to be updated in the file:")
        with open(file , 'w') as file1:
            file1.write(content)
    elif(choice == 4):
        if(os.path.exists(file)):
            os.remove(file)
        else:
            print("The file doesn't exists")
    else:
        print("Enter the valid choice!")
    num = int(input("If you want to continue enter any number other than zero:"))
print("Thank you!")
