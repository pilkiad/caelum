"""
> Global variables

This module contains variables needed / shared by multiple other modules.

environment
===========

We store two types of function definitions in the environment: a primitive
function and custom functions.
1. Primitive functions are those that reference inbuilt functions like int or
    print. When these functions are defined (a = int(0)) we simply store their
    output in the environment for easy access.
2. Custom functions contain a code block (my_func = { }). In this case we store
    all or their information in the environment.
"""

# TODO - create environment.py instead

from .function_definition import FunctionDefinition


VERSION = "a-2"
environment: list[list[FunctionDefinition]] = [[]]

