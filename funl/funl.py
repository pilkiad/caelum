"""
Entry point to funl, currently used for testing
"""

from textx import metamodel_from_str

from funl import mm_definition as mmd
from funl import evaluator

# Example input
input_code: str = """
a = int(2)
b = uint(-3)

result = add(a(), b())

print(cast(result(), str))
"""

# Parse the input string
model = mmd.mm.model_from_str(input_code)

# Evaluate the parsed model
evaluator.eval_model(model)
