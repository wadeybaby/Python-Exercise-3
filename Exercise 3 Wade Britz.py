# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print('Hello World!')
# TODO: Call the 'greet' function
greet()
#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
name= input('Enter name: ')
def p_greeting():
    print(f'Hello {name}')
# TODO: Call the 'personalized_greeting' function with your name
p_greeting()

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
num = int(input('Enter the number: '))
def square(num):
    result = num**2
    return result
# TODO: Call the 'square' function with the number 5 and print the result
print(square(num))

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    return length * width 
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
rec_length = 4
rec_width = 5
print(f'The area of the rectangle is: {rectangle_area(rec_length, rec_width)}')
#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(func, number):
    return func(number)
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(num_1):
    return num_1 * 2 
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
result_double = apply_operation(double,7)
print(result_double)
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
result_square = apply_operation(square,3)
print(result_square)
