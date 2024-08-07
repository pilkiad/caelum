"""
Provides functionality for evaluating funl functions
"""

import typing

from funl import mm_definition as mmd
from funl.utils import logger
from funl.functions import funl_add
from funl.functions import funl_int
from funl.functions import funl_print
from funl.functions import funl_cast

# TODO - comment
# comes from evaluator
environment: dict[str, mmd.mm["FunctionCall"]] = {}


def eval_function(
    name: str, params: list[mmd.mm["Param"]] | None
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
        function: mmd.mm["Function"] = get_function(name=name)
        if function is None:
            logger.err("VALUE", f"Unknown token '{name}'")
        else:
            # TODO -    fails because now codeblocks can be defined,
            #           and now these block dont match the syntax we expect
            #           here: they have no name(params) pattern but we need to
            #           simply evaluate them (turn them into statements)
            # NOTE -    Maybe now we need to implement a stack?
            return eval_function(name=function.name, params=function.params)

    return None


def get_function(name: str) -> mmd.mm["FunctionCall"] | None:
    """
    Gets a user defined function from the environment

    name: str   The name of the function

    mmd.mm['FunctionCall'] | None:  The metamodel function if one was found
                                    None otherwise
    """

    assert(name is not None)

    global environment

    for key, value in environment.items():
        if key == name:
            return value

    return None
