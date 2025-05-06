from functools import lru_cache
import time

def factorial_normal(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

@lru_cache(maxsize=None)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# factorial_normal(100)
# factorial(100)

start_time = time.time()
factorial_normal(100)  # Test with a larger number to see the difference
end_time = time.time()
print(f"Time for normal factorial: {end_time - start_time:.5f} seconds")

# Measure execution time for cached factorial function
start_time = time.time()
factorial(100)  # Test with the same number
end_time = time.time()
print(f"Time for cached factorial: {end_time - start_time:.5f} seconds")