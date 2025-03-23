"""
> Interprets caelum models

This is the heart of the caelum language.

This module will handle all interpretative work when handling .clm files.
Since everything in caelum is either a function definition or declaraction, there
are not that many individual functions in this module.

This is the general behaviour:
1. The entry point is always interpret_model(), both for a new file or a custom
    function being called withing the file
2. From there, call _evaluate_expression() for every line of code within the model
3. This will call either _evaluate_function_call() or _evaluate_function_definition()
    3.1 _evaluate_function_call() will either call a handle() function if the function
        being called is native, return its value if its primitive or execute the
        code block if its custom
    3.2 _evaluate_function_definition() will parse the function definition to
        the environment handler

There are three types of functions known in caelum:
    - **native** functions, builtins like println, int, ...
    - **custom** functions, defined by the user like: my_func=(){...}
    - **primitive** functions, special case of custom functions where the function
        is equal to a single native call like: x=int(0)
"""

from .utils import logger
from .utils import globalvars
from .utils import environment
from . import parser
from .utils import grammar
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
from .functions import f_sub
from .functions import f_assert
from .functions import f_float
from .functions import f_rfloat
from .functions import f_str
from .functions import f_bool
from .functions import f_rbool
from .functions import f_meh
from .functions import f_arr
from .functions import f_draw
from .functions import f_arr_push
from .functions import f_arr_set
from .functions import f_eq
from .functions import f_gt
from .functions import f_lt
from .functions import f_div
from .functions import f_and
from .functions import f_or
from .functions import f_xor
from .functions import f_clear
from .functions import f_import


# FUNCTION_MAP contains references to each inbuilt funl functions handler functions
# See functions/ fo all inbuilts
FUNCTION_MAP = {
    "print": f_print.handle,
    "int": f_int.handle,
    "add": f_add.handle,
    "in": f_in.handle,
    "eval": f_eval.handle,
    "exit": f_exit.handle,
    "rint": f_rand.handle,
    "println": f_println.handle,
    "version": f_version.handle,
    "return": f_return.handle,
    "sub": f_sub.handle,
    "assert": f_assert.handle,
    "float": f_float.handle,
    "rfloat": f_rfloat.handle,
    "str": f_str.handle,
    "bool": f_bool.handle,
    "rbool": f_rbool.handle,
    "meh": f_meh.handle,
    "arr": f_arr.handle,
    "draw": f_draw.handle,
    "arr_push": f_arr_push.handle,
    "arr_set": f_arr_set.handle,
    "eq": f_eq.handle,
    "lt": f_lt.handle,
    "gt": f_gt.handle,
    "div": f_div.handle,
    "and": f_and.handle,
    "or": f_or.handle,
    "xor": f_xor.handle,
    "clear": f_clear.handle,
    "import": f_import.handle
}

# Keeps track of the current call hirarchy depth
depth: int = 0

def interpret_model(model: any, inline: bool = False) -> any:
    """
    Interprets any funl textx.Model!

    model: textx.Model  The model to be executed
    inline: bool        Whether or not the model shall NOT create a new environment
                        Set to True when evaluating model defined in eval as the code
                        specified should run in the same environment as the parent function

    Returns the model itself or its return value if explicitly defined
    """

    if not inline:
        global depth
        depth += 1

    for statement in model.statement:
        logger.log_debug("Interpreter", f"interpret_model: {statement}")

        result = _evaluate_expression(statement)

        # If return() was called the entire code block returns the result of
        # that statement
        if statement.name == "return":
            if not inline:
                depth -= 1
                environment.pop()

            return result

    # This gets called when we ran through an entire code block (function) without
    # an explicit return. However it should not be called on the first code block
    # (which is the entire application)
    if not inline:
        if depth > 1:
            environment.pop()
        depth -= 1

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
    if statement.name != "eval":
        evaluated_params = [_evaluate_expression(param) for param in statement.params]
    else:
        evaluated_params = [_evaluate_expression(statement.params[0])]
        evaluated_params.append(statement.params[1])

    # Check if the function is native
    if statement.name in FUNCTION_MAP:
        function_call = FUNCTION_MAP[statement.name]
        return _evaluate_native_function_call(
            statement.name, function_call, evaluated_params
        )

    # Check if the function is custom
    function_call = environment.get_function_from_name(statement.name)
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
    if name == "eval" or name == "import":
        resulting_model = handler(params)
        if resulting_model is None:
            return None
        return interpret_model(resulting_model, inline=True)

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
    # computed on definition, i.e. int()
    if statement.code_block is None and statement.params_out is not None:
        logger.log_debug("Interpreter", "... (function is primitive)")
        # Special case: primitive function calls to arrays can accept an index as parameter
        if len(params) != 0 and isinstance(statement.params_out, list) and isinstance(params[0], int):
            # TODO - improve and add check for bounds
            return statement.params_out[params[0]]
        else:
            return statement.params_out

    # Custom functions first need all of the input parameters put into the
    # current environment
    if hasattr(statement, "params_in") and statement.params_in is not None:
        logger.log_debug("Interpreter", "... (function is custom)")

        # Before creating the parameters, we need to create a new environment in
        # which the called function will operate
        environment.new()

        # Check if the correct number of parameters is given as input in the call
        if len(params) != len(statement.params_in):
            logger.log_error(
                "Interpreter",
                f"Incorrect parameters for '{statement.name}'. Got: {params} Expected: {statement.params_in}",
            )

        # Compute all input parameters
        for i in range(0, len(statement.params_in)):
            result = FunctionDefinition(
                name=statement.params_in[i], params_out=params[i]
            )
            logger.log_debug("Interpreter", f"... -> {result}")
            environment.append_or_update(result)

        # Call the new code block (will be textx.model) with the params now in env
        return _evaluate_expression(statement.code_block)

    # FIXME - some functions may return None right now
    # i believe there should be a custom datatype to represent "nothing"
    # or we need to disallow non-initialized variables by design
    logger.log_error("Interpreter", f"Tried to call undefined: {statement}")


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
        environment.append_or_update(
            FunctionDefinition(
                name=statement.name,
                params_out=_evaluate_function_call(statement.function),
            )
        )

    # Custom functions are defined with a code block and parameters that reference
    # variables to that needs to be stored
    elif statement.code_block is not None:
        environment.append_or_update(
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
    CURRENTLY OBSOLETE, KEPT BECAUSE WE MIGHT NEED THIS AT SOME POINT

    Calls a custom function based on the function name provided as string
    Usually called by eval()

    name: str   Name of the function, can be None
    """

    logger.log_debug("Interpreter", f"... _function_from_string: {name}")

    function_call = environment.get_function_from_name(name)

    # Check if the function actually exists
    if function_call is not None and function_call.code_block is not None:
        # Make sure the function has a local environment
        environment.new()
        # Call and return the function
        return interpret_model(function_call.code_block)

    # Can't raise an error if no name was given,
    # because eval() may return None if evaluated statement is false
    if name is not None:
        logger.log_error("Interpreter", f"Tried to call invalid function: {name}")
