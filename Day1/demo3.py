#!/usr/bin/env python3
# Script to demonstrate usage of decorators
import functools
# Log the function call
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments= {args}")
        result = func(*args, **kwargs)
        print(f"function {func.__name__} finished. Result:  {result}")
        return result
    return wrapper

@log_function
def greet(name):
    return "Hello "+ name

#decorated_greet = log_function(greet)

print(greet("Vishwas"))

#print(decorated_greet("Jane"))