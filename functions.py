#!/bin/env python3
import math


def float_range(start=0.0, end=0.0, step=1.0):
    while start < end:

        yield start
        start += step


def combine_funcs(func_1, func_2, function_name=None):
    def inner(*args, **kargs):
        return func_2(func_1(*args, **kargs))

    if function_name is not None:
        inner.__name__ = function_name

    return inner


def for_every_element(elements, func, *args, **kargs):
    results = []
    for element in elements:
        results.append(func(element, *args, **kargs))


def print_result(x, func):
    print(x, '->', func(x))


def print_results_for_function(elements, func):
    return for_every_element(elements, print_result, func)


def print_table(list_of_elements, func_1, func_2, decimal_places=3):
    top = f"| {'x':>15} | {func_1.__name__:>15} | {func_2.__name__:>15} |"
    delimiter = len(top) * '-'

    print(top)
    print(delimiter)

    for element in list_of_elements:
        x_str = format(element, f'.{decimal_places}f')
        result_1 = format(func_1(element), f'.{decimal_places}f')
        result_2 = format(func_2(element), f'.{decimal_places}f')

        row = f'| {x_str:>15} | {result_1:>15} | {result_2:>15} |'
        print(row)

    print(delimiter)


def main():
    two_x_exp = combine_funcs(lambda x: 2*x,
                            lambda x: 2**x,
                            function_name='two_x_exp')

    squared_exp = combine_funcs(lambda x: 2**x,
                                lambda x: x**2,
                                function_name='squared_exp')


    list_of_elements = float_range(start=-9, end=2, step=0.5)
    print_table(list_of_elements, two_x_exp, squared_exp)


if __name__ == '__main__':
    main()
