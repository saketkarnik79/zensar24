# Program Name: HelloWorld
# Author: Saket Karnik
# Version: 1.0

"""
This program demonstrates
a multi-line comment.
"""

print("Hello, World!"); # This displays "Hello, World!" on terminal

# This displays "Welcome to Python Program!" on terminal.
print("Welcome to Python Program!");

def greet(name):
    """Displays a welcome message.""" # This is docstring for the function greet()
    print("Welcome, " + name)

greet("Saket Karnik");

print(greet.__doc__);