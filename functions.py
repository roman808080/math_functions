#!/bin/env python3
import math


def combine_funcs(func_1, func_2):
    def inner(*args, **kargs):
        return func_2(func_1(*args, **kargs))

    return inner


def for_every_element(func, elements, *args, **kargs):
    results = []
    for element in elements:
        results.append(func(element, *args, **kargs))


def print_result(x, func):
    print(x, '->', func(x))


def print_results_for_function(func, elements):
    return for_every_element(print_result, elements, func)


two_x_exp = combine_funcs(lambda x: 2*x,
                          lambda x: 2**x)

squared_exp = combine_funcs(lambda x: 2**x,
                            lambda x: x**2)


list_of_elements = [-2, -1, -0.5, 0, 0.5, 1, 2]

print('two_x_exp')
print_results_for_function(two_x_exp, list_of_elements)
print()

print('squared_exp')
print_results_for_function(squared_exp, list_of_elements)
print()
