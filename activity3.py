class IOstring():

     #constructor to set default value
     def __init__(self):
          self.str1 = ""
    #function to print the string in upper case
     def get_string(self):
          self.str1 = input("Enter string")
     def print_string(self):
          print("result is :",self.str1.upper())
# object creation
str1 = IOstring()
#call functions
str1.get_string()
str1.print_string()
