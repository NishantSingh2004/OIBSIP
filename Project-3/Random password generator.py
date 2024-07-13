import random
import string
import sys  #

def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters  # contains all lowercase and uppercase letters
    digits = string.digits  # contains 0-9 as digit characters in form of string
    special_chars = string.punctuation

    characters = letters  # created the variable 'characters' that holds the string from another variable 'letters' which contains all the different characters we could be selecting from (('cus we've added other characters - digits & special_chars through string concatenation. So, characters includes more characters now)
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    password = ""
    meets_criteria = False
    has_number = False
    has_special_chars = False

    while not meets_criteria or len(password) < minimum_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_chars = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special_chars

    return password  # immediately returns password when the while loop conditions are false like it meets criteria and minimum password length is correct


while True:
    minimum_length = input("Enter the minimum length (or type 'exit' to quit): ")
    if minimum_length.lower() == 'exit':
        print("Thank you for stopping by! Exiting the program...")
        sys.exit()
    try:
        minimum_length = int(minimum_length)
        if minimum_length > 0:
            break
        else:
            print("Minimum length must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number for minimum length or correct your spelling of 'exit'.")

# minimum_length = int(input ("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (yes/no): ").lower() == "yes"
has_special_chars = input("Do you want to have special characters? (yes/no): ").lower() == "yes"

password = generate_password(minimum_length, has_number, has_special_chars)
print("The generated password is:", password)