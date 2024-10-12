"""
> Global variables

This module contains variables needed / shared by multiple other modules
"""

from .function_definition import FunctionDefinition


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
