# # # #There are these following datatyes in Python
# # # Integer : int (1, 10, 100)
# # # Floating point: float (1.0, 10.0, 100.0)
# # # Strings : str ('hello', "Hello", '10')
# # # Lists : list  ([10, "hello", 200.3])
# # # Dictionaries: dict ({"mykey":"value","name":"Sam"})
# # # Tuples : tup ((10, "hello", 200.3))
# # # Sets : set ({"a", "b"})
# # # Booleans :bool (True or False)
# # a = 2
# # b = 3
# # sum(a+b)
# # print(sum)

# # # Datatypes, numbers, operations, Type Conversion, f-strings
# # #Primitive Datatypes:
# # print(len("Hello")) #To find length of the character

# # #Types and error:
# # #print(len(12345)) ##This will show error (Type error: object of type 'int' has no len())

# # # num_char = len(input("Whats your name ? : "))
# # #print("Your name has" + num_char + "characters")  #Type error: can only concatenate str (not "int") to str
# # # print(type(num_char))

# # ## The solution to above error can be written as:
# # num_char = len(input("Whats your name ? : "))
# # new_num_char = str(num_char)
# # print("Your name has" + " " + new_num_char + " " +"characters")  

# a = float(123)
# print(type(a))

# print(70 + float("100.5")) #Converting string into float and adding 70 

# print(str(70) + str(100)) #ans: 70100


# # a = 123
# # print(type(a)) # integer

# # b = str(123)
# # print(type(b))

# # ## Datatypes:

# # ## String
# # print("Hello")
# # print("Hello"[0]) #To print the 1st character i.e. zero index aka subscripting
# # print("123" + "456") #concatinates 

# # ##Integer 
# # print(123)
# # print(123+345) #Calculates

# # ##Float 
# # print(3.1234)

# # ##Boolean
# # ##True or False

# # a = input("What is your name ?: ")
# # b = str(len(a))
# # print("The length of your name" + " " + a +" " + "is" + " " + b)


# ######Code challenge######
# ## Write a program that adds the digit in 2 digit number. e.g. if the input was 35 then the output should be 3 + 5 = 8
# ##Solution:
# two_digit_number = input("Enter a 2 digit number: ")

# first_digit_number = int(two_digit_number[0])
# second_digit_number = int(two_digit_number[1])

# #Add the two integer together
# two_digit_number = first_digit_number + second_digit_number

# print(two_digit_number )


sum_of_two_digit = input("Please enter a valid 2 digit number: ")
first_input = int(sum_of_two_digit[0])
second_input = int(sum_of_two_digit[1])
sum = first_input + second_input

print(sum)