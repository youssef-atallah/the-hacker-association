# Level 4: Functions & Modules
# Topics: Function Definitions, Arguments, Return Values, Importing Modules
# Exercises:
# 1. Write a function that reverses a string.
# 2. Check if a password is strong (≥8 chars, includes number & special character).
# 3. Generate a random password of 12 characters.
# 4. Create an MD5 hash of a user-entered string using hashlib.
# 5. Check if an IP address is valid.
# 6. Generate random MAC addresses.
# 7. XOR encryption function.
# 8. Generate a random device ID using uuid.
# 9. Resolve a hostname to an IP address.
# 10. Extract all vowels from a string.



#? 1. Write a function that reverses a string.

def string_revers(string):
  return string[ : :-1]

print(string_revers('Hello'))



#? 2. Check if a password is strong (≥8 chars, includes number & special character).

import string

def password_check(paswrd):
  strong = False

  if len(paswrd) < 8:
    return 'Not Strong'

  includes_numbers = False
  includes_special_char = False

  for i in paswrd:
    if i in string.punctuation:
      includes_special_char = True

    if i in string.digits:
      includes_numbers = True
  

  if includes_numbers == True and includes_special_char == True:
    strong = True

  
  return 'Strong' if strong else 'Not Strong'

print(password_check('helloA1@') )

# improved versions:
# 1: 
  # import string

  # def password_check(paswrd):
  #     has_length = len(paswrd) >= 8
  #     has_letter = any(char in string.ascii_letters for char in paswrd)
  #     has_digit = any(char in string.digits for char in paswrd)
  #     has_special = any(char in string.punctuation for char in paswrd)

  #     return has_length and has_letter and has_digit and has_special

  # # Example
  # print(password_check("Hello@123"))  # True
  # print(password_check("weak"))       # False

# 2:
  # import string

  # def password_check(paswrd):
  #     if len(paswrd) < 8:
  #         return 'Not Strong'

  #     includes_numbers = any(i in string.digits for i in paswrd)
  #     includes_special_char = any(i in string.punctuation for i in paswrd)

  #     return 'Strong' if includes_numbers and includes_special_char else 'Not Strong'

  # print(password_check('helloA1@')) 



#? 3. Generate a random password of 12 characters.

import random
import string

def random_pass():
  char = ''
  for i in range(12):
    char += random.choice(string.ascii_letters + string.digits + string.punctuation)
  
  return char

print(random_pass())

# improved verstions:
  # 1      - Use random.choices() for brevity and performance:

    # def random_pass():
    #   return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
  

  # 2.       - Ensure at least one character of each type (for stronger passwords):
  
      # def strong_random_pass():
      #     chars = [
      #         random.choice(string.ascii_lowercase),
      #         random.choice(string.ascii_uppercase),
      #         random.choice(string.digits),
      #         random.choice(string.punctuation)
      #     ]
      #     chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=8)
      #     random.shuffle(chars)
      #     return ''.join(chars)

      # print(strong_random_pass())


# 4. Create an MD5 hash of a user-entered string using hashlib.

import hashlib

def MD5_hash(user_str):
    return hashlib.md5(user_str.encode()).hexdigest()

print(MD5_hash('Hello')) 

    # user_str.encode() converts the string to bytes.

    # .hexdigest() converts the hash to a readable hexadecimal string.



  #     return 'Strong' if includes_numbers and includes_special_char else 'Not Strong'
#? 5. Check if an IP address is valid.

import string

def IP_check(ip):
    has_letter = any(char in string.ascii_letters for char in ip)
    has_invalid_special = any(char in string.punctuation.replace('.', '') for char in ip) # Exclude the dot (.) from the special characters check

    return 'Not Valid' if has_letter or has_invalid_special else 'Valid'

print(IP_check('192.168.1.1'))      
print(IP_check('192.168.1.a'))      
print(IP_check('192.168.1.1$'))      

# improved verstion:
    # Proper IP address validation using logic
    #  check 4 numbers between 0–255 separated by dots:

def IP_check(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return 'Not Valid'
    for part in parts:
        if not part.isdigit():
            return 'Not Valid'
        if not 0 <= int(part) <= 255:
            return 'Not Valid'
    return 'Valid'

print(IP_check('192.168.1.1'))     # Valid
print(IP_check('256.100.1.1'))     # Not Valid (256 is too high)
print(IP_check('192.abc.1.1'))     # Not Valid (letters)
print(IP_check('192.168.1.'))      # Not Valid (missing part)





#? 6. Generate random MAC addresses
import random

def random_mac():
    mac = [f"{random.randint(0, 255):02X}" for _ in range(6)]
    return ":".join(mac)

print(random_mac()) 

# random.randint(0, 255) generates a number from 0 to 255.
# :02X formats the number as a 2-digit uppercase hex.
    # 3B:44:C9:0E:6E:16
    # F7:71:DF:75:51:21
    # 9B:04:9B:E4:12:0B

# more:
#  Generate locally administered unicast MAC (common practice):
# The second least significant bit of the first byte should be 1 (locally administered), and the least significant bit should be 0 (unicast). Here's how:

def random_mac_locally_admin():
    first_byte = random.randint(0, 255)
    # Set locally administered bit (bit 1) to 1 and unicast bit (bit 0) to 0
    first_byte = (first_byte & 0b11111100) | 0b00000010

    mac = [first_byte] + [random.randint(0, 255) for _ in range(5)]
    return ":".join(f"{b:02X}" for b in mac)

print(random_mac_locally_admin()) 





#? 7. XOR encryption function
def xor_encrypt_decrypt(input_str, key):
    # Convert both strings to byte arrays
    input_bytes = input_str.encode()
    key_bytes = key.encode()

    output_bytes = bytearray()

    for i in range(len(input_bytes)):
        # XOR each byte with the corresponding key byte (loop key if shorter)
        output_bytes.append(input_bytes[i] ^ key_bytes[i % len(key_bytes)])

    # Return result as hex string (for readability)
    return output_bytes.hex()

def xor_decrypt(hex_str, key):
    encrypted_bytes = bytes.fromhex(hex_str)
    key_bytes = key.encode()

    output_bytes = bytearray()

    for i in range(len(encrypted_bytes)):
        output_bytes.append(encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)])

    return output_bytes.decode()

key = "mysecret"
text = "Hello World!"

encrypted = xor_encrypt_decrypt(text, key)
print("Encrypted:", encrypted)

decrypted = xor_decrypt(encrypted, key)
print("Decrypted:", decrypted)





#? 8. Generate a random device ID using uuid.

import uuid

def generate_device_id():
    return str(uuid.uuid4())

print(generate_device_id()) 






# 9. Resolve a hostname to an IP address.

import socket

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Hostname could not be resolved."

print(resolve_hostname("www.google.com"))  
print(resolve_hostname("facebook.com"))  
print(resolve_hostname("invalid.hostname"))  



#? 10. Extract all vowels from a string.
def extract_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char in vowels])

print(extract_vowels("Hello World"))  # Output: eoO
print(extract_vowels("Hello super H"))   # eoue
