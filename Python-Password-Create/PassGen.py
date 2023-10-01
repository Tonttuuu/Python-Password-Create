import random
import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "[]{}()*;/:-"

all_chars = lower + upper + numbers + symbols
length = 16

password = "".join(random.sample(all_chars, length))

password_name = input("Give name for password: ")

with open('passwords.txt', 'a') as f:
    original_stdout = sys.stdout
    sys.stdout = f

    print(f"Name: {password_name}")
    print(f"Password: {password}")
    print("----------------------------------------------------------\n")

    sys.stdout = original_stdout

