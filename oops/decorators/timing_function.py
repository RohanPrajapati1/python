# Write a decorator that measure the time a function takes to execute

import time

def timer(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    print(f"Finished sleeping for {n} seconds.")

example_function(2)