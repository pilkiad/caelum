"""
Entry point to funl, currently used for testing
"""

from textx import metamodel_from_str
import typing

from funl import mm_definition
from funl import evaluator

# Example input
input_code: str = """
a = int(40)
b = int(2)
res = add(a(), b())
print(
    "a + b = ",
    cast(a(), str),
    " + ",
    cast(b(), str),
    " = "
    cast(res(), str)
)
"""

# Parse the input string
model = mm_definition.mm.model_from_str(input_code)

# Evaluate the parsed model
evaluator.eval_model(model)
