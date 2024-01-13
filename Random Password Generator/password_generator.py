import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user-defined criteria.
    Parameters:
    - length: Length of the password
    - use_letters: Include letters in the password
    - use_numbers: Include numbers in the password
    - use_symbols: Include symbols in the password"""
    
    # Define character sets based on user preferences
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure at least one character set is selected
    if not characters:
        print("Error: At least one character set must be selected.")
        return None

    # Generate password using random.choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Take input from the user
    length = int(input("Enter the password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    # Display the generated password
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()