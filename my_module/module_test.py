# module_example.py

def greet_user(username):
    """Greet the user by username."""
    greeting = f"Hello, {username}! Welcome to the simulation."
    print(greeting)

def add_numbers(first_number, second_number):
    """Add two numbers and print the result."""
    result = first_number + second_number
    print(f"The sum of {first_number} and {second_number} is {result}.")

def print_message():
    """Print a predefined message."""
    message = "This is a test message from your script."
    print(message)

if __name__ == "__main__":
    # Example usage
    greet_user("Alice")
    add_numbers(5, 3)
    print_message()
