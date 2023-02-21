# Passing a func as a parameter:

def apply_func(numbers, func):
    """Apply a given function to a list of numbers."""
    result = []
    for num in numbers:
        result.append(func(num))
    return result
def square(x):
    """Return the square of a number."""
    return x**2
# In this example, we define a function apply_func that takes a list of numbers and a 
# function as parameters. The function apply_func applies the given function to each number in
# the list and returns a list of the results.
# We also define two functions square and cube that take a number as input and return its 
# square and cube, respectively. We then call the apply_func function twice, once
# with the square function and once with the cube function, to demonstrate how you can 
# pass different functions as parameters to the same function.
# Apply the square function to a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_func(numbers, square)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

