# module_test.py

def add_numbers(a, b):
    result = a + b
    print(f"Adding {a} + {b} = {result}")
    return result

def multiply_numbers(a, b):
    result = a * b
    print(f"Multiplying {a} * {b} = {result}")
    return result

def print_message(message):
    print(f"Message: {message}")

def run_all():
    # Calls other functions with predefined arguments
    add_numbers(5, 3)  # Example call
    multiply_numbers(4, 2)  # Example call
    print_message("Hello from GitHub Actions")  # Example call
