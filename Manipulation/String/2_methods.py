# Code with Harry: https://www.youtube.com/watch?v=0INvoK_T0cE

# NOTES:
# - strings are immutable

# length of a string
print(len("Sankalp"))

# make all char upper case (no inplace change)
name = "Sankalp"
print(name.upper())

# make all char lower case 
print(name.lower())

# What if
str = "Sankalp!!!"
print(str.upper())

# Capitalize: makes the first letter capital, also makes remaining lower
heading = "Introduction to python"
print(heading.capitalize())

heading = "IntroducTion to pYTHON"
print(heading.capitalize())

# Remove '!' characters
print(str.rstrip('!'))

# Replace all occurances of "Sankalp" with "Sanky"
print(str.replace("Sankalp", "Sanky"))

# Spliting strings and returns a list of strings
fullname = "Sankalp Naveenachandra Kulkarni"
print(fullname.split(" "))

# Count number of times "Sankalp" has occured - CASE SENSITIVE (regex)
names = "Sankalp Kulkarni Sankalp Sanky Snakalp Sankalp"
print(names.count("Sankalp"))
print(names.count("sankalp"))
print(names.count("Sank"))

# endswith(): boolean
print(str.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith('to', 4, 10))   # str, start, end index

# find(): int, returns the index of the first occurance of a string
str1 = "Welcome to the ConsoleWelcome to the ConsoleWelcome to the Console"
print(str1.find("to"))

# index(): 
str1 = "Welcome to the ConsoleWelcome to the ConsoleWelcome to the Console"
print(str1.index("to"))

# isalnum(): boolean, alpha numerics
print(str1.isalnum())

# islower(), isupper()
print(str1.islower())

# isprintable(): boolean, returns true is only alpha numeric (no white spaces)
print(str1.isprintable())
str1 = "Welcome to \t the ConsoleWelcome to the ConsoleWelcome to the Console"
print(str1.isprintable())

# istitle(): boolean, 
title = "To Kill A Mockingbird"
print(title.istitle())

# startswith(): boolean

# swapcase(): toggle bw upper and lower

# title(), converts to title format



