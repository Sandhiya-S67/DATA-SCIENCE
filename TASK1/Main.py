import os
print("List of files Before:")
print(os.listdir())
print("\n")
with open("file1.txt" , "r") as file1:
  with open("file2.txt" , "w") as file2:
    file2.write(file1.read())
with open("file2.txt" , "r") as file2:
  print(file2.read())
print("List of files after:")
print(os.listdir())
print("\n")
