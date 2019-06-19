#Exercise 5
#define class which as at least 2 methods:
#getString, printString


class InputOutString(object):
    def _init__(self):
       self.x = ""

    def getString(self):
        self.x = input("Provide a list of school subjects: ")

    def printString(self):
        print(self.x.upper())

strObj = InputOutString()
strObj.getString()
#looks for the user input from def getString(self)
#another way to look for input instead of x=input("User input")
strObj.printString()
#prints the input out with all caps from the def printString(self)




