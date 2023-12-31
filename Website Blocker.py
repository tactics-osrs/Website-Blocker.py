import string
import random

def generate_password(length, use_special_chars):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    # Use the random.choice function to select characters at random
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    # Ask the user to input the length of the password
    length = int(input("Enter the length of the password you want to generate: "))

    # Ask the user if they want to include special characters
    use_special_chars = input("Do you want to include special characters? (yes/no): ")
    use_special_chars = use_special_chars.lower() == 'yes'

    # Generate a password of the user-specified length
    print(generate_password(length, use_special_chars))

    restart = input("Press enter to Restart or type 'quit' to Exit: ")
    if restart.lower() == 'quit':
        break
