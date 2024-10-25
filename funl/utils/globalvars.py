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

# TODO - make environment a list

from .function_definition import FunctionDefinition


VERSION = "a-0"
environment: list[FunctionDefinition] = []


def get_function_from_name(name: str) -> FunctionDefinition | None:
    for environment_function in environment:
        if environment_function.name == name:
            return environment_function
    return None


def get_function_index_from_name(name: str) -> int | None:
    for i in range(0, len(environment)):
        if environment[i].name == name:
            return i
    return None


def append_or_update(function_definition: FunctionDefinition) -> None:
    result = get_function_index_from_name(function_definition.name)

    if result is not None:
        environment[result] = function_definition
    else:
        environment.append(function_definition)
