"""
Provides functionality for evaluating textx models
"""

from funl import mm_definition
from funl.utils import eval_function as ef

environment: dict[str, mm_definition.mm["Function"]] = {}
last_statement = None


def eval_model(model) -> None:
    # TODO - type annotation
    global last_statement
    global environment

    ef.environment = environment
    for statement in model.statement:
        last_statement = statement
        eval_statement(statement)


def eval_statement(statement: str):
    # TODO - type annotation
    if isinstance(statement, mm_definition.mm["FunctionDefinition"]):
        eval_function_definition(statement.name, statement.function)
    if isinstance(statement, mm_definition.mm["Function"]):
        ef.eval_function(statement.name, statement.params)


def eval_function_definition(
    name: str, function: mm_definition.mm["FunctionDefinition"]
) -> None:
    # TODO - type annotation
    global environment
    environment.update({name: function})
    ef.eval_function(name=function.name, params=function.params)
