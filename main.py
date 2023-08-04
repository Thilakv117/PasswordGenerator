import string
import random

def get_password(min_len, number = True, special = True):
    characters = string.ascii_letters
    number = string.digits
    special_characters = string.punctuation
    if number:
        characters += number
    if special:
        characters += special_characters
    
    random_password = ''.join(random.choice(characters) for _ in range(min_len))
    return random_password
def main():
    password_length = int(input("Enter the length of a password: "))
    password = get_password(password_length)
    print(password)
main()