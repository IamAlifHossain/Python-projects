import random
import string
print()
print("Welcome to the password generator program!")
print()
pass_length = int(input("Enter the length of password: "))
characters = string.ascii_letters + string.digits + string.punctuation + " "
password = ""
for i in range(0, pass_length):
    password += random.choice(characters)

print(f"Your password is: {password}")
