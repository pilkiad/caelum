"""
> Manages the environments in which funl functions operate

This class provides an interface to create or find functions in the current environment
aswell as create and pop environments.
This is currently used by the interpreter when calling function or returning from them.
"""

from . import logger
from . import globalvars
from .function_definition import FunctionDefinition


def get_function_from_name(name: str, index: int = -1) -> FunctionDefinition | None:
    """
    Returns FunctionDefinition searched by a given name

    name: str   The name to search for
    index: int  The starting level of environment hirarchy, will begin locally
                and work its way up to global env

    FunctionDefinition if the function was found,
    None otherwise
    """

    for environment_function in globalvars.environment[index]:
        if environment_function.name == name:
            return environment_function

    # If we did not find the function, try an upper level environment
    if index != len(globalvars.environment) * -1:
        return get_function_from_name(name, index=(index-1))
    else:
        return None


def get_local_function_index_from_name(name: str) -> int | None:
    """
    Fetches a custom function index inside of its environment
    Will default to the current environment but an environment index can be specified

    name: str   The name of the function
    
    NOTE - The function index (level of environment) can only ever be -1 as this
    function is usually just called by append_or_update() which may only happen
    at the current level of environment depth

    Returns the index of the function in its environment if found,
    None otherwise
    """

    # Search in the environment with the specified index
    for i in range(0, len(globalvars.environment[-1])):
        # Go through all entries in the environment
        if globalvars.environment[-1][i].name == name:
            return i

    return None


def append_or_update(function_definition: FunctionDefinition) -> None:
    """
    Will append or update the function given to the current environment

    function_definition: FunctionDefinition The function to be updated or appended
                                            if it does not already exist
    """

    result = get_local_function_index_from_name(function_definition.name)

    if result is not None:
        logger.log_debug("Environment", f"append_or_update => update {function_definition.name}")
        globalvars.environment[-1][result] = function_definition
    else:
        logger.log_debug("Environment", f"append_or_update => append {function_definition.name}")
        globalvars.environment[-1].append(function_definition)


def new() -> None:
    """
    Creates a new level of the environment
    Typically called when a custom function was called in the interpreter
    """

    logger.log_debug("Environment", f"new (depth: {len(globalvars.environment)+1})")

    globalvars.environment.append([])


def pop() -> None:
    """
    Removes the current layer of environment
    Typically called when a custom function has returned in the interpreter

    Errors on trying to pop global environment
    """
    
    logger.log_debug("Environment", f"pop (depth: {len(globalvars.environment)-1})")

    if len(globalvars.environment) == 1:
        logger.log_info("Environment", "Did you call 'return()' outside of a function?")
        logger.log_error("Environment", "Tried to pop the global environment")

    globalvars.environment.pop()