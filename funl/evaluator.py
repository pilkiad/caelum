"""
Provides functionality for evaluating textx models
"""

import typing
from textx import metamodel_from_str

from funl import mm_definition
from funl.utils import eval_function as ef

environment: dict[str, mm_definition.mm["Function"]] = {}
last_statement = None

def eval_model(model) -> None:
    """
    Evaluates a textx model

    model: textx?Model  The model to evaluate
    """

    global last_statement
    global environment

    ef.environment = environment
    for statement in model.statement:
        last_statement = statement
        eval_statement(statement)


def eval_statement(statement: str):
    """
    Evaluates a single statement within a textx model

    statement: textx?Statement  The statement to evaluate
    """

    if isinstance(statement, mm_definition.mm["FunctionDefinition"]):
        reveal_type(statement)
        eval_function_definition(statement.name, statement.function)
    if isinstance(statement, mm_definition.mm["Function"]):
        ef.eval_function(statement.name, statement.params)


def eval_function_definition(
    name: str, function: mm_definition.mm["FunctionDefinition"]
) -> None:
    """
    Evaluate a function definition within a textx model
    
    name: textx?Function.Name       The name of the function
    function: textx?Function.Params The parameters of the function
    """

    global environment

    environment.update({name: function})
    ef.eval_function(name=function.name, params=function.params)
