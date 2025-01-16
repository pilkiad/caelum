"""
> Container for custom defined functions

This class contains information about functions the user defined in their code.
Example:
my_func = () {}
needs to store:
- function name
- input params
- code block
- output param(s)
"""


class FunctionDefinition:
    def __init__(
        self,
        name: str,
        code_block: any = None,
        params_in: list[any] = None,
        params_out: list[any] = None,
    ):
        self.name = name
        self.code_block = code_block
        self.params_in = params_in
        self.params_out = params_out

    def __str__(self) -> str:
        return f"{self.name} = in({self.params_in}) out({self.params_out})"
