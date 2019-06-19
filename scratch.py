#Exercise 5
#define class which as at least 2 methods:
#getString, printString


class createstring(object):
    def _init_(self):
        self.x = ""

    def getString(self):
        self.x = input("Please list different types of fruit:")

    def printString(self):
        print(self.x.upper())

strObj = createstring()
strObj.getString()
strObj.printString()



