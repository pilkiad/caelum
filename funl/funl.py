"""
Entry point to funl, currently used for testing
"""

from textx import metamodel_from_str

from funl import mm_definition as mmd
from funl import evaluator
from funl.utils import logger

# Example input
input_code: str = """
print("Hello, world!")
"""

# Parse code to logger so we can find some infos one the statements later on
logger.input_code = input_code

# Parse the input string
model = mmd.mm.model_from_str(input_code)

# Evaluate the parsed model
evaluator.eval_model(model)

print("")
