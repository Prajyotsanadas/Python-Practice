# #To print Hello World
# print("Hello World")

# # #Python Variables 
##The name of the variable has to be 1 single unit. (name , user_name, name1, etc.)
##The variable name must not contain space, number at beginning (user name, 1name, etc)

# #Taking input in variable from user
# name = input("What is your name? : ") #This takes data from user
# print (name)

#Variables can be changed
name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("Whats your name? :")
length = len(name)
print(length) # This finds the length of your name

#Code challenge: 
#There are 2 variables : a and b, Write a program that switches the value stored in the variables a and b.
a = input()
b = input()

c = a # Creating a third variable will help switch the input
a = b
b = c 

print("a: " + a)
print("b: " + b)


