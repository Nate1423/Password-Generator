import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    # Characters to choose from
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters

    # Ensure password has at least one letter, one digit, and one symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage:
password_length = int(input("Enter password length: "))
print("Generated password:", generate_password(password_length))
