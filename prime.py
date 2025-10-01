import math

def is_prime(n):
    # Handle edge cases for numbers less than or equal to 1
    if n <= 1:
        return False
    # Check divisibility by 2 first
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check divisibility from 3 to sqrt(n), skipping even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")   
