# TODO - add module comment

from . import logger
from . import globalvars
from .function_definition import FunctionDefinition


def get_function_from_name(name: str, index: int = -1) -> FunctionDefinition | None:
    for environment_function in globalvars.environment[index]:
        if environment_function.name == name:
            return environment_function

    if index != len(globalvars.environment) * -1:
        return get_function_from_name(name, index=(index-1))
    else:
        return None


def get_function_index_from_name(name: str, index: int = -1) -> int | None:
    """
    Fetches a custom function index inside of its environment
    Will default to the current environment but an environment index can be specified

    name: str   The name of the function
    index: int  The index of the environment, default: -1 to select the current
                local environment

    The index of the function in its environment if found,
    None otherwise
    """

    # Search in the environment with the specified index
    for i in range(0, len(globalvars.environment[index])):
        # Go through all entries in the environment
        if globalvars.environment[index][i].name == name:
            return i

    # FIXME - i do not know why i wrote this or what it does
    #if index != len(globalvars.environment) * -1:
    #    logger.log_error("environment", "what")
    #    return get_function_from_name(name, index=(index-1))
    #else:
    return None


def append_or_update(function_definition: FunctionDefinition) -> None:
    # NOTE - no possibility to change the index here since writing should only
    # be possible to the current scope
    result = get_function_index_from_name(function_definition.name)

    if result is not None:
        logger.log_debug("environment", f"append_or_update => update {function_definition.name}")
        globalvars.environment[-1][result] = function_definition
    else:
        logger.log_debug("environment", f"append_or_update => append {function_definition.name}")
        globalvars.environment[-1].append(function_definition)


def new() -> None:
    """
    Creates a new level of the environment.
    Typically called when a custom function was called in the interpreter.
    """

    logger.log_debug("environment", f"new (depth: {len(globalvars.environment)+1})")

    globalvars.environment.append([])


def pop() -> None:
    """
    Removes the current layer of environment.
    Typically called when a custom function has returned in the interpreter.
    """
    # TODO - Does return() call this?

    logger.log_debug("environment", f"pop (depth: {len(globalvars.environment)-1})")

    globalvars.environment.pop()