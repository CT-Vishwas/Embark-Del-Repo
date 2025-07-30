#!/usr/bin/env python3
# Timing Decorator
import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time: .4f} seconds to execute.")
        return result
    return wrapper


@timing_decorator
def long_run_task():
    time.sleep(5)
    return "Task Completed"

print(long_run_task())