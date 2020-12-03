import time

"""
Functions are the first classs objects in python, meaning, they can be treated just like any other variable and can be passed as argument to another function or even return them as a return value
"""


def time_it(func):
    """Decorator to time the calculations of certain task
       It allows to wrap one function into another function
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            func.__name__
            + " funciton took "
            + str(round(((end - start) * 1000), 2))
            + " ms to run."
        )
        return result

    return wrapper


@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

# output of this file
"""
calc_square funciton took 11.97 ms to run.
calc_cube funciton took 14.19 ms to run.
"""

