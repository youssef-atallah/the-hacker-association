# 10. Given a dictionary of usernames and passwords, write a script that asks for a username
    # and prints the stored password.

users = {'youssef': 'y0xPass123', 'ahmed': 'ah/pass02'}

def users_dictionary():
  username = input("Enter your username: ")

  print(f'{username},  your password is: {users[username]}')



users_dictionary()