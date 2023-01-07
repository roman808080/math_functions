#!/bin/env python3
import math


def combine_funcs(func_1, func_2):
    def inner(*args, **kargs):
        return func_2(func_1(*args, **kargs))

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
    for element in list_of_elements:
        result_1 = format(func_1(element), f'.{decimal_places}f')
        result_2 = format(func_2(element), f'.{decimal_places}f')

        row = f'| {result_1:>10} \t | {result_2:>10} \t|'
        print(row)

two_x_exp = combine_funcs(lambda x: 2*x,
                          lambda x: 2**x)

squared_exp = combine_funcs(lambda x: 2**x,
                            lambda x: x**2)


list_of_elements = [-2, -1, -0.5, 0, 0.5, 1, 2]

print_table(list_of_elements, two_x_exp, squared_exp)

# print('two_x_exp')
# print_results_for_function(list_of_elements, two_x_exp)
# print()

# print('squared_exp')
# print_results_for_function(list_of_elements, squared_exp)
# print()
