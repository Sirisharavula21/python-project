def is_palindrome(string):
    """Check if a string is a palindrome."""
    string = string.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return string == string[::-1]

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')