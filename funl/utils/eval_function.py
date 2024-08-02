"""
Provides functionality for evaluating funl functions
"""

import typing

from funl import mm_definition
from funl.utils import logger
from funl.functions import funl_add
from funl.functions import funl_int
from funl.functions import funl_print
from funl.functions import funl_cast

# TODO - comment
# comes from evaluator
environment: dict[str, mm_definition.mm["Function"]] = {}


def eval_function(
    name: str, params: list[mm_definition.mm["Param"]] | None
) -> typing.Any:
    """
    Evaluates (executes) a function

    name: str                               The name of the function
    params: list[mm['Param']] | None        Function parameters, can be empty

    Any:    Returns whatever the evaluated function returns
    """

    global environment

    if name == "add":
        return funl_add.handle(params)
    elif name == "int":
        return funl_int.handle(params)
    elif name == "print":
        return funl_print.handle(params)
    elif name == "cast":
        return funl_cast.handle(params)
    else:
        function: mm_definition.mm["Function"] = get_function(name=name)
        if function is None:
            logger.err("VALUE", f"Unknown token '{name}'")
        else:
            return eval_function(name=function.name, params=function.params)

    return None


def get_function(name: str) -> mm_definition.mm["Function"] | None:
    """
    Gets a user defined function from the environment

    name: str   The name of the function

    mm['Function'] | None:  The metamodel function if one was found
                            None otherwise
    """

    global environment

    for key, value in environment.items():
        if key == name and isinstance(value, mm_definition.mm["Function"]):
            return value

    return None
