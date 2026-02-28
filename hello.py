print('Hello, World!') # This prints a greeting message

print("Hello world") # Also this prints a greeting message

print('ciao', 'gigi', sep = '[separatore]', end= '[questo alla fine]') # This prints a greeting message with a separator and an end

print(f"Valore 1: {my_var_1}, valore 2: {my_var_2}") # This prints the values of my_var_1 and my_var_2

print(f"Valore 1: {}, valore 2: {}".format(my_var_1, my_var_2)) # This also prints the values of my_var_1 and my_var_2 using the format method

my_var = 1 # This assigns an integer value to my_var

my_var = 1.1 # This assigns a float value to my_var

my_var = True # This assigns a boolean value to my_var

my_var = 'Hello' # This assigns a string value to my_var

my_var = [1, 2, 3] # This assigns a list to my_var

my_var = (1, 2, 3) # This assigns a tuple to my_var

my_var = {1, 2, 3} # This assigns a set to my_var

my_var = {'key1': 'value1', 'key2': 'value2'} # This assigns a dictionary to my_var

my_var = None # This assigns a None value to my_var, indicating that it has no value

#Type function return type of the variable
print(type(my_var)) # This prints the type of my_var, which is NoneType

###
### This is a multi-line comment

x = 5
y = 10

#Aritmetical operations
x==y # This checks if x is equal to y and returns a boolean value
x != y # This checks if x is not equal to y and returns a boolean value
x > y # This checks if x is greater than y and returns a boolean value
x < y # This checks if x is less than y and returns a boolean value
x >= y # This checks if x is greater than or equal to y and returns a boolean value
x <= y # This checks if x is less than or equal to y and returns a boolean value

#Boolean operations
x < y and y > 5 # This checks if x is less than y and y is greater than 5
x < y or y > 15 # This checks if x is less than y or y is greater than 15
not(x < y) # This negates the boolean value of (x < y)

x = "3" # This assigns a string value to x
print(x+x) # This concatenates the string x with itself and prints "33"
print(2*x) # This repeats the string x twice and prints "33"

#some symbols in string are interpreted differently e.g. \n for newline
print("Hello\nWorld") # This prints "Hello" and "World" on separate lines
print("Hello\tWorld") # This prints "Hello" and "World" with a tab space in between

#we can access to the string using indexing
my_string = "Hello, World!"
print(my_string[0]) # This prints the first character of the string my_string
print(my_string[1]) # This prints the second character of the string my_string
print(my_string[-1]) # This prints the last character of the string my_string

print(my_string[0:5]) # This prints the substring from index 0 to 4 of my_string, which is "Hello"
print(my_string[7:]) # This prints the substring from index 7 to the end of my_string, which is "World!"
print(my_string[:5]) # This prints the substring from the start to index 4 of my_string, which is "Hello"
print(my_string[1:10:2]) # This prints the substring from index 1 to 9 of my_string with a step of 2, which is "el,W"
print(my_string[::2]) # This prints the substring of my_string with a step of 2, which is "Hlo ol!"
print(my_string[::-1]) # This prints the reverse of my_string, which is "!dlroW ,olleH"

#casting (if a conversion is not possible, it will raise an error)
my_var = 1 # This assigns an integer value to my_var
print(float(my_var)) # This casts my_var to a float and prints 1.0
print(str(my_var)) # This casts my_var to a string and prints "1"

#input function allows us to get user input from the console
user_input = input("Enter something: ") # This prompts the user to enter something
print("You entered:", user_input) # This prints the user's input

#if condition
if user_input:
    print("You entered something!")
else:
    print("You didn't enter anything.")

#we can nest if statements
if user_input:
    print("You entered something!")
    if user_input == "Hello":
        print("You entered Hello!")
    else:
        print("You didn't enter Hello.")

#we can use elif for multiple conditions
if user_input == "Hello":
    print("You entered Hello!")
elif user_input == "Goodbye":
    print("You entered Goodbye!")
else:
    print("You entered something else.")


#while loop
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit): ")
    print("You entered:", user_input)

#for loop
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print("Iteration:", i)

#range function generates a sequence of numbers
#range(start, stop, step)
for i in range(1, 10, 2):
    print("Odd number:", i)

#enumerate function adds a counter to an iterable and returns it as an enumerate object
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)

#Defining a function
def my_function(param1, param2):
    print("Parameter 1:", param1)
    print("Parameter 2:", param2)

my_function("Hello", "World") # This calls the function my_function with the arguments "Hello" and "World" but doesn't return anything.

#Returning a value
def my_function(param1, param2):
    print("Parameter 1:", param1)
    print("Parameter 2:", param2)
    return param1 + " " + param2

result = my_function("Hello", "World") # This calls the function my_function and stores the returned value in result
print("Result:", result) # This prints the result

#Function with default parameter values
def my_function(param1, param2="World"):
    print("Parameter 1:", param1)
    print("Parameter 2:", param2)

my_function("Hello") # This calls the function my_function with the argument "Hello" and uses the default value for param2


