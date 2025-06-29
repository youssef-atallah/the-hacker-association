
# Level 2: Control Flow & Loops
# Topics: If-else, For loops, While loops, Logical Operators
# Exercises:
# 1. Write a script that asks for a password and only allows access if it matches "s3cr3t".
# 2. Print all numbers from 1 to 100 except numbers divisible by 4.
# 3. Print every 4-digit PIN code (0000–9999).
# 4. Check if a given year is a leap year.
# 5. Find prime numbers between 1 and 100.
# 6. Simulate a login system that locks after 3 failed attempts.
# 7. Create a number guessing game.
# 8. Print numbers 1-100, replacing multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz".
# 9. Continuously ask for a password until the correct one is entered.
# 10. Check if a string is a palindrome



#! Code:

# 1. Write a script that asks for a password and only allows access if it matches "s3cr3t".

user_pass = 'temp'
while True:
	user_pass = input("Enter Your Password: ")

	if user_pass == 's3cr3t':
		print("Welcome to our system")
		break
	else:
		print("Wrong Password")

    ## improved version
    # MAX_ATTEMPTS = 3
    # attempts = 0

    # while attempts < MAX_ATTEMPTS:
    #     user_pass = input("Enter Your Password: ")
        
    #     if user_pass == 's3cr3t':
    #         print("Welcome to our system")
    #         break
    #     else:
    #         attempts += 1
    #         print(f"Wrong Password. You have {MAX_ATTEMPTS - attempts} attempts left.")

    # if attempts == MAX_ATTEMPTS:
    #     print("Too many wrong attempts. Access denied.")



# 2. Print all numbers from 1 to 100 except numbers divisible by 4.
for i in range(100):
    if i % 4 != 0:
        print(i, end=" ")



# 3. Create a script that prints every 4-digit PIN code (0000-9999).

PIN_code = '00009999'
j = 0
for i in range(len(PIN_code) ):
	j +=1
	print(PIN_code[i], end="")
	if j == 4 and len(PIN_code) - (i + 1) != 0 : # len(PIN_code) - (i + 1) != 0 -> to avoid printing - at the end 
		print(end="-")
		j = 0

    # Improved Version
    # PIN_code = '00009999'

    # for i, digit in enumerate(PIN_code):
    #     print(digit, end="")
    #     if (i + 1) % 4 == 0 and i != len(PIN_code) - 1:
    #         print(end="-")



# 4. Check if a given year is a leap year.

# Leap Year Rules:
# A year is a leap year if:

# It is divisible by 4, and:

# It is not divisible by 100, unless:

# It is divisible by 400.
    # Improved Version
    # year = 2024
    # if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # 	print(f"this year:{year} is a leap year ")
    # else:
    # 	print(f"this year:{year} is not a leap year ")

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# 5. Find prime numbers between 1 and 100.

import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no divisors found, it's prime

# Find and print prime numbers between 1 and 100
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")



# 6. Simulate a login attempt system that locks after 3 failed attempts.
passwd = 'temp'
attempts = 0 
while True:
    if attempts >= 3:
        print("Failed to login, you have reached the maximum attempts")
        break

    passwd = input("Enter Your Password: ")

    if passwd == 's3cr3t':
        print("Welcome to our system")
        break
    else:
        print("Wrong Password")
        attempts += 1


# 7. Create a basic number guessing game.
import random
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")



# 8. FizzBuzz implementation
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")



# 9. Use a while loop to continuously ask for a password until the correct one is entered.
while True:
    user_pass = input("Enter Your Password: ")
    if user_pass == 's3cr3t':
        print("Welcome to our system")
        break
    else:
        print("Wrong Password")


# 10. Check if a string is a palindrome (same forward and backward).
text = input("Enter the text: ")
if text == text[::-1]:
    print("Yes Palindrome")
else:
    print("NO Not Palindrome")
    
  # short if
  # print("Yes Palindrome" if text == text[::-1] else "NO Not Palindrome")