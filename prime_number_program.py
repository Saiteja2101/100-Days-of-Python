import math

def is_prime(num):
    """
    Checks whether a given number is a prime number.
    Returns True if the number is prime, False otherwise.
    """
    # 1. Handle Edge Cases
    # Numbers less than 2 are not prime. 1 is not prime by definition.
    if num < 2:
        return False
    
    # 2. Check for Divisibility up to the Square Root
    # We only need to check for divisors up to the square root of the number (inclusive).
    # If a number has a divisor greater than its square root, it must also have a divisor 
    # smaller than its square root.
    
    # Calculate the integer part of the square root
    limit = int(math.sqrt(num))
    
    # Check for divisibility by all integers from 2 up to the calculated limit
    for i in range(2, limit + 1):
        if num % i == 0:
            # If the number is evenly divisible by any number other than 1 and itself, 
            # it is not prime.
            return False
    
    # If the loop finishes without finding any divisors, the number is prime.
    return True

print(is_prime(71))
print(is_prime(24))
print(is_prime(75))