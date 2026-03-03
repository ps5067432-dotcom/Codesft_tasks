import random
import string

print("=== Strong Password Generator ===")

# Step 1: Take user input
length = int(input("Enter the desired password length: "))

if length < 4:
    print("Password length should be at least 4 for better security.")
else:
    # Step 2: Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Step 3: Generate password
    password = ""
    for i in range(length):
        password += random.choice(all_characters)

    # Step 4: Display password
    print("\nGenerated Password:", password)