"""
> Interprets funl models

NOTE - currently WIP until I finally get my head around how recursive interpretation
works
"""

from .utils import logger
from .utils import globalvars
from .utils.function_definition import FunctionDefinition

from .functions import f_print
from .functions import f_int
from .functions import f_add
from .functions import f_in
from .functions import f_eval
from .functions import f_exit
from .functions import f_rand
from .functions import f_println
from .functions import f_version
from .functions import f_return


# FUNCTION_MAP contains references to each inbuilt funl functions handler functions
# See functions/ fo all inbuilts
FUNCTION_MAP = {
    "print": f_print.handle,
    "int": f_int.handle,
    "add": f_add.handle,
    "in": f_in.handle,
    "eval": f_eval.handle,
    "exit": f_exit.handle,
    "rand": f_rand.handle,
    "println": f_println.handle,
    "version": f_version.handle,
    "return": f_return.handle,
}


def interpret_model(model: any) -> any:
    """
    Interprets any funl textx.Model!

    model: textx.Model

    Returns the model itself (usefull for some recursion stuff later down the
    line?)
    """

    for statement in model.statement:
        logger.log_debug("Interpreter", f"interpret_model: {statement}")

        result = _evaluate_expression(statement)

        if statement.name == "return":
            return result

    return model


def _evaluate_expression(statement: any) -> any:
    """
    Handler function for all expressions
    Simply calls the responsible - more specific - handler functions

    statement: textx.Statement
    """

    logger.log_debug("Interpreter", f". _evaluate_expression: {statement}")

    if statement.__class__.__name__ == "Model":
        return interpret_model(statement)
    if statement.__class__.__name__ == "FunctionCall":
        return _evaluate_function_call(statement)
    if statement.__class__.__name__ == "FunctionDefinition":
        return _evaluate_function_definition(statement)
    else:
        return statement


def _evaluate_function_call(statement: any) -> any:
    """
    Handler function for native and custom function calls
    Simply evaluates their parameters and gives the info to the corresponding
    handler function

    statement: textx.FunctionCall

    Returns whatever the function call returned
    """

    logger.log_debug("Interpreter", f".. _evaluate_function_call: {statement.name}")

    # All parameters of function calls should be evaluated before calling
    evaluated_params = [_evaluate_expression(param) for param in statement.params]

    # Check if the function is native
    if statement.name in FUNCTION_MAP:
        function_call = FUNCTION_MAP[statement.name]
        return _evaluate_native_function_call(
            statement.name, function_call, evaluated_params
        )

    # Check if the function is custom
    function_call = globalvars.get_function_from_name(statement.name)
    if function_call is not None:
        return _evaluate_custom_function_call(function_call, evaluated_params)

    if function_call is None:
        logger.log_error(
            "Interpreter", f"Calling an unknown function: {statement.name}"
        )


def _evaluate_native_function_call(name: str, handler: any, params: any) -> any:
    """
    Handler function for native function calls (print, int, ...)

    name: str   The name of the native function
    handler: any    The handler function for the native function,
                    i.e functions/print.handle
    params: any     List of parameters to be given the function,
                    have to be previously evaluated

    Returns whatever the native function call returned
    """

    logger.log_debug("Interpreter", f"... _evaluate_native_function_call: {name}")

    # Special case eval: the return value has to be
    if name == "eval":
        return _call_function_from_string(handler(params))

    return handler(params)


def _evaluate_custom_function_call(statement: FunctionDefinition, params: any) -> any:
    """
    Handler function for primitive or custom function calls (functions defined
    by the user). Will evaluate a custom function as a textx.Model

    statement: textx.FunctionCall
    params: any                     List of parameters to be given the function,
                                    have to be previously evaluated

    Returns primitive function output in case of primitive function call
    Returns textx.Model in case of custom function call
    """

    logger.log_debug(
        "Interpreter", f"... _evaluate_custom_function_call: {statement.name}"
    )

    # Primitive functions simply return their output parameter that has been
    # computed on definition
    if statement.code_block is None and statement.params_out is not None:
        logger.log_debug("interpreter", "... (primitive)")
        return statement.params_out

    # Custom functions first need all of the input parameters put into the
    # current environment
    if hasattr(statement, "params_in") and statement.params_in is not None:
        logger.log_debug("interpreter", "... (custom)")

        if len(params) != len(statement.params_in):
            logger.log_error(
                "interpreter",
                f"Incorrect parameters for '{statement.name}'. Got: {params} Expected: {statement.params_in}",
            )

        for i in range(0, len(statement.params_in)):
            result = FunctionDefinition(
                name=statement.params_in[i], params_out=params[i]
            )
            globalvars.environment.append(result)

        # Call the new code block (will be textx.model) with the params now in env
        return _evaluate_expression(statement.code_block)

    logger.log_error("interpreter", "this should not happend")


def _evaluate_function_definition(statement: any) -> None:
    """
    Handler function for when the user defines a function

    statement: textx.FunctionDefinition
    """

    logger.log_debug(
        "Interpreter", f".. _evaluate_function_definition: {statement.name}"
    )

    # Primitive functions simply store their output parameter for later user
    if statement.function is not None:
        globalvars.append_or_update(
            FunctionDefinition(
                name=statement.name,
                params_out=_evaluate_function_call(statement.function),
            )
        )

    # Custom functions are defined with a code block and parameters that reference
    # variables to that needs to be stored
    elif statement.code_block is not None:
        globalvars.append_or_update(
            FunctionDefinition(
                name=statement.name,
                code_block=statement.code_block,
                params_in=statement.params,
            )
        )

    else:
        logger.log_error(
            "Interpreter", f"Invalid function definition: {statement.name}"
        )


def _call_function_from_string(name: str) -> any:
    """
    Calls a custom function based on the function name provided as string

    name: str   Name of the function, can be None
    """

    logger.log_debug("Interpreter", f"... _function_from_string: {name}")

    function_call = globalvars.get_function_from_name(name)

    if function_call is not None and function_call.code_block is not None:
        return interpret_model(function_call.code_block)

    # Can't raise an error if no name was given,
    # because eval() may return None if evaluated statement is false
    if name is not None:
        logger.log_error("Interpreter", f"Tried to call invalid function: {name}")
