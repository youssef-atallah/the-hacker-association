# 🔥 Level 3: Lists, Tuples, and Dictionaries
# Topics: Indexing, Iteration, Dictionary Lookups
# 🔹 Exercises:
# 1. Create a list of 10 hacker tools (["Nmap", "Metasploit", "Wireshark", "Burp
# Suite", "JohnTheRipper", ...]).
# 2. Print the 3rd item in the list.
# 3. Create a dictionary storing common HTTP status codes and their meanings (e.g.,
# {200: "OK", 404: "Not Found"}).
# 4. Write a program that counts how many times each letter appears in a string.
# 5. Sort a list of random numbers without using .sort().
# 6. Store ports and their corresponding services in a dictionary and allow the user to
# query by port number.
# 7. Write a function that removes duplicates from a list.
# 8. Convert a list into a comma-separated string.
# 9. Write a function that finds the longest word in a list.
# 10. Given a dictionary of usernames and passwords, write a script that asks for a username
    # and prints the stored password.

# 1
hacker_tools = ["Nmap", "Metasploit", "Wireshark", "Burp Suite", "JohnTheRipper", "Metasploit", "Wireshark", "Burp Suite", "JohnTheRipper", "Metasploit", "Wireshark", "Burp Suite", "JohnTheRipper"]


# 2
print(hacker_tools[2])


# 3
http_status_codes = {200: "OK", 404: "Not Found"}


# 4 
str  = "Hello World"
print(str.count("l"))



# 5 
# Bubble Sort
lst = [4, 2, 3, 1, 5]
n = len(lst)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)

# Here are the names of various sorting algorithms:
  # 1. Bubble Sort
  # 2. Selection Sort
  # 3. Insertion Sort
  # 4. Merge Sort
  # 5. Quick Sort
  # 6. Heap Sort
  # 7. Counting Sort
  # 8. Radix Sort
  # 9. Timsort
  # 10. Bucket Sort




# 6 
ports_and_services = {80: "HTTP", 443: "HTTPS", 22: "SSH", 21: "FTP", 25: "SMTP"}



# 7. Write a function that removes duplicates from a list.

lst = ['yusuf', 'ali', 'veli', 'yusuf','selami', 'ali' , 'ali', 'ayşe', 'fatma', 'hayriye', 'ayşegül', 'ayşe', 'fatma', 'hayriye', 'ayşegül', 'ayşe', 'fatma', 'hayriye', 'ayşegül']

new_lst = []
# 7 
def remove_duplicates(lst):
    for i in lst:
        if i not in new_lst:
          new_lst.append(i) 
    return new_lst

print(remove_duplicates(lst))


print(lst)



# Best Practices
    # 1- Use set() for Simplicity (Unordered):

    # Convert the list to a set and back to a list. This is efficient but does not preserve the order of elements.

    # lst = [1, 2, 3, 4, 3, 2]
    # unique_lst = list(set(lst))
    # print(unique_lst)  # Output: [1, 2, 3, 4] (order may vary)
    ## using a set will not preserve the original order of elements. 


    # 2- Use dict.fromkeys() for Ordered Results:

    # Since Python 3.7+, dictionaries maintain insertion order. This method removes duplicates while preserving the original order.

    # lst = [1, 2, 3, 4, 3, 2]
    # unique_lst = list(dict.fromkeys(lst))
    # print(unique_lst)  # Output: [1, 2, 3, 4]



# 8 Convert a list into a comma-separated string.

my_list = ['ali', 'youssef', 'muhammad', 'salah']

print(','.join(my_list))



# 9. Write a function that finds the longest word in a list.
my_list = ['ali', 'youssef', 'muhammad', 'salah']

def largest_word(lst):
  largest_word_is = ''
  for i in lst:
    if len(i) > len(largest_word_is):
      largest_word_is = i
  return largest_word_is

print(largest_word(my_list) )



# 10. Given a dictionary of usernames and passwords, write a script that asks for a username
    # and prints the stored password.

users = {'youssef': 'y0xPass123', 'ahmed': 'ah/pass02'}

def users_dictionary():
  username = input("Enter your username: ")

  print(f'{username},  your password is: {users[username]}')



users_dictionary()