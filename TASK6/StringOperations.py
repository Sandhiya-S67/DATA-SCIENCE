class String:
    def __init__(self , mystring):
        self.mystring = mystring
    
    def StringSplit(self):
        splittedString = mystring.split(" ")
        print(f"The string after the split:{splittedString}")
        return splittedString

    def StringConcat(self , splittedString):
        result = "-".join(splittedString)
        print(f"The string concatination using hypen(-):{result}")

mystring = input("Enter the string:")
st = String(mystring)
splittedString = st.StringSplit()
st.StringConcat(splittedString)
