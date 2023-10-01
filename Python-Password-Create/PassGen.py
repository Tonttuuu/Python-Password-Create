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

    print(f"Nimi: {password_name}")
    print(f"Salasana: {password}")
    print("----------------------------------------------------------\n")

    sys.stdout = original_stdout

