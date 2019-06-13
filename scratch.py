#Exercise 4
#takes in a sequence of comma separated numbers
#generate a list and tuple which contains every number
#example 34,67,55,33,12,98

n = input("Enter a list of numbers")
x=n.split(",") #split is the function for how you want to split the sequence
#by comma, by word, by semicolon
t=tuple(x)
print(t)



