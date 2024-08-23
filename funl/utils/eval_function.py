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
from funl.functions import funl_uint

# TODO - comment
# comes from evaluator
environment: dict[str, mmd.mm["FunctionCall"]] = {}
# FIXME - kind of ugly structure i think
# Guaranteed to be global
global_environment: dict[str, mmd.mm["FunctionCall"]] = {}


def eval_function(name: str, params: list[mmd.mm["Param"]] | None) -> typing.Any:
    """
    Evaluates (executes) a function call.
    A function call can have the form of one of the following:
    1. Primitive call, like 'add' or 'int'
        - In this case, call the handle() function provided by funl to
            execute the inbuilt functionality
    2. A custom defined function, like 'x = int(5)'
        - In this case, whenever we find the name 'x' simply call eval_function again
            in order to evaluate the primitive
    3. A custom defined code block, like 'my_func = { ... }'
        - In this case, turn everything inside the code block into a model and
            start executing that

    So, function calls are sort of handled recursively. Execute every
    function until we have reached a primitive

    name: str                               The name of the function
    params: list[mm['Param']] | None        Function parameters, can be empty

    Any:    Returns whatever the evaluated function returns
    """

    global environment

    # Check if we are evaluating a primitive function
    if name == "add":
        return funl_add.handle(params)
    elif name == "int":
        return funl_int.handle(params)
    elif name == "print":
        return funl_print.handle(params)
    elif name == "cast":
        return funl_cast.handle(params)
    elif name == "uint":
        return funl_uint.handle(params)

    # If not, are we looking at a custom defined function?
    else:
        function: mmd.mm["Function"] = get_function(name=name)

        # If there is neither a primitive or a custom function being called,
        # the user must have entered something invalid
        if function is None:
            logger.err(
                "VALUE",
                f"Unknown token '{name}'",
                [
                    "You may have misspelled the name",
                    "You may have declared thevariable in a local scope",
                ],
            )
            return

    # Check if function has params or codeblock
    if hasattr(function, "params"):
        return eval_function(name=function.name, params=function.params)
    else:
        # Evaluate a code block as a new model
        from funl import evaluator

        evaluator.eval_code_block_as_model(function)


def get_function(name: str) -> mmd.mm["FunctionCall"] | None:
    """
    Gets a user defined function from the environment

    name: str   The name of the function

    mmd.mm['FunctionCall'] | None:  The metamodel function if one was found
                                    None otherwise
    """

    assert name is not None

    global environment
    global global_environment

    # Search local environment for var
    # (if there is a local env)
    if environment is not None:
        for key, value in environment.items():
            if key == name:
                return value

    # Search global environment for var
    for key, value in global_environment.items():
        if key == name:
            return value

    return None
