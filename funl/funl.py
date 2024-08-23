"""
Entry point to funl, currently used for testing
"""

from textx import metamodel_from_str

from funl import mm_definition as mmd
from funl import evaluator

# Example input
input_code: str = """
a = int(0)

my_func = {
    b = int(1)

    print("a() from global env: ")
    print(cast(a(), str), n)
    print("b() from local env: ")
    print(cast(b(), str), n)
}

my_func()

print("Printing b() should error, since function was left: ", n)
print(cast(b(), str))
"""

# Parse the input string
model = mmd.mm.model_from_str(input_code)

# Evaluate the parsed model
evaluator.eval_model(model)

print("")
