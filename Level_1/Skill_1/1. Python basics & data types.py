# opics: Variables, Data Types, Strings, Numbers, Booleans, Input/Output
# Exercises:
# 1. Print "Hello, Hacker!" to the console.
# 2. Ask the user for their name and print "Welcome, [name]!".
# 3. Convert "1337" (string) to an integer and add 10.
# 4. Create a program that asks for two numbers and prints their sum, difference, product,
# and quotient.
# 5. Reverse the string "rekcah_repus" without using built-in functions.
# 6. Write a program that checks if a number is even or odd.
# 7. Create a variable that stores a boolean value and print it.
# 8. Convert the string "100101" to a decimal number.
# 9. Print "H4ck3r" with alternating uppercase and lowercase letters.
# 10. Replace all vowels in "P@ssw0rd" with "*".



#! Code:
# Level 1: Python Basics & Data Types

# 1. Print "Hello, Hacker!" to the console.
print("Hello, Hacker!")

# 2. Ask the user for their name and print "Welcome, [name]!".
name = input("Enter Your Name: ")
print(f"Welcome, {name}")

# 3. Convert "1337" (string) to an integer and add 100.
str = "1337"
str_to_int = int(str) + 100

# 4. Create a program that asks for two numbers and prints their sum, difference, product, and quotient.
f_num, s_num = map(int, input("Enter Two Numbers: ").split())
print(f"The Sum of two numbers is: {f_num + s_num}")
print(f"The Subtraction of two numbers: {f_num - s_num}")
print(f"Multiplication of two numbers: {f_num * s_num}")
print(f"Division Of two numbers: {f_num / s_num}")

# 5. Reverse the string "rekcah_repus" without using built-in functions.
original_text = "rekcah_repus"
print(original_text[::-1])

# 6. Write a program that checks if a number is even or odd.
number = 5
print(f"{number} is Even" if number % 2 == 0 else f"{number} is Odd")

# 7. Create a variable that stores a boolean value (True or False) and print it.
boolean_val = True
print(boolean_val)

# 8. Convert the string "100101" to a decimal number.
the_string = "100101"
str_to_decimal = float(the_string)
print(f"string to decimal: {str_to_decimal}")

# 9. Print "H4ck3r" with alternating uppercase and lowercase letters.
normal_text = "H4ck3r"
print(f"Upper case: {normal_text.upper()}")
print(f"Lower case: {normal_text.lower()}")

# 10. Given password = "P@ssw0rd", replace all vowels with "*".
password = "P@ssw0rd"
print(f'the password is: {len(password) * "*"}')