#!/usr/bin/python3
"""
Script that computes the minimum operations
needed in a Copy All - Paste task
"""

def minOperations(n):
    """
    Method for computing the minimum number
    of operations for task Copy All and Paste
    Args:
        n: input value
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_sum = 0
    i = 2  # Start with the first prime number
    while n > 1:
        while n % i == 0:
            factor_sum += i
            n //= i  # Use integer division
        i += 1
    return factor_sum

# Example usage
if __name__ == "__main__":
    result = minOperations(12)
    print("Minimum operations:", result)