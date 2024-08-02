from textx import metamodel_from_str
import typing

funl_grammar = """
    Model: statement *= Statement;

    Statement: FunctionDefinition | Function;

    FunctionDefinition: name=ID '=' function=Function;
    Function: name=ID '(' params*=Param (',' params*=Param)* ')';

    Param: Function | INT | ID | STRING;
    Comment: /#.*$/;
    ID: /[a-zA-Z_][a-zA-Z0-9_]*/;
    INT: /[0-9]+/;
    STRING: /".*"/;
"""

# Create a metamodel from the grammar
metamodel = metamodel_from_str(funl_grammar)

# Example input
input_code = '''
a = int(2)
b = int(3)
res = add(a(), b())
print("a + b = ", cast(res(), str))
'''

# Parse the input string
model = metamodel.model_from_str(input_code)

# Environment to store variable values
environment = {}
last_statement = None

# Function implementations

def err(errtype: str, reason: str) -> None:
    print(f"ERROR.{errtype}: {reason}")
    exit(1)

def assert_type(func: str, value: any, expected: type) -> bool:
    """
    Checks if a given value is of the correct datatype and reports an error
    if that is not the case

    func: str       The inbuilt function that wants to assert the type,
                    used for error printing
    value: any      The value we want to check the type of
    expected: type  The type the variable should have

    bool:           Returns True if type is correct,
                    False otherwise
    """

    if value is None:
        err("INCORRECT_TYPE",
            f"Function '{func}' expected type "
            f"'{expected.__name__}' but got "
            f"none")
        return False

    result = isinstance(value, expected)

    if not result:
        err("INCORRECT_TYPE",
            f"Function '{func}' expected type "
            f"'{expected.__name__}' but got "
            f"'{type(value).__name__}'")
        return False

    return True

def int_function(params) -> int:
    if params == None or len(params) == 0:
        err("INCORRECT_PARAMS", "Missing parameters for function 'int'")
    assert_type("int", params[0], int)

    return int(params[0])

def add_function(params: list[metamodel["Param"]] | None) -> int:
    if params == None or len(params) == 0:
        err("INCORRECT_PARAMS", "Missing parameters for function 'add'")

    result = 0

    for param in params:
        value = param
        if isinstance(param, metamodel["Function"]):
            value = eval_function(name=param.name, params=param.params)

        assert_type("add", value, int)
        result += value

    return result

def print_function(params: list[metamodel["Param"]] | None) -> str:
    """
    Inbuilt function
    Prints all parameters to stdout
    """

    if params == None or len(params) == 0:
        err("INCORRECT_PARAMS", "Missing parameters for function 'print'")
    
    result = ""

    for param in params:
        value = param
        if isinstance(param, metamodel["Function"]):
            value = eval_function(name=param.name, params=param.params)
        
        assert_type("print", value, str)
        print(value, end="")
        result += value

    print("")
    return result

def cast_function(params: list[metamodel["Param"]] | None) -> any:
    """
    Inbuilt function
    Casts params[0] to type params[1]
    """

    if params == None or len(params) != 2:
        err("INCORRECT_PARAMS", "Missing parameters for function 'cast'")
    assert_type("cast", params[0], metamodel["Function"])
    assert_type("cast", params[1], str)

    if params[1] == "str":
        return str(eval_function(name=params[0].name, params=params[0].params))
    elif params[1] == "int":
        return int(eval_function(name=params[0].name, params=params[0].params))

    err("INCORRECT_TYPE", f"Cannot cast to '{params[1]}'")

# Function map
function_map = {
    "int": int_function,
    "add": add_function,
    "print": print_function,
    "cast": cast_function
}

def eval_model(model):
    global last_statement
    for statement in model.statement:
        last_statement = statement
        eval_statement(statement)

def eval_statement(statement):
    if isinstance(statement, metamodel["FunctionDefinition"]):
        eval_function_definition(statement.name, statement.function)
    if isinstance(statement, metamodel["Function"]):
        eval_function(statement.name, statement.params)

def eval_function_definition(name: str, function: metamodel["FunctionDefinition"]) -> None:
    global environment
    environment.update({name: function})
    eval_function(name=function.name, params=function.params)

def eval_function(name: str, params: list[metamodel["Param"]] | None) -> any:
    """
    Evaluates (executes) a function

    name: str                               The name of the function
    params: list[metamodel["Param"]] | None Function parameters, can be empty
    """

    if name == "add":
        return add_function(params)
    elif name == "int":
        return int_function(params)
    elif name == "print":
        return print_function(params)
    elif name == "cast":
        return cast_function(params)
    else:
        function: metamodel["Function"] = get_function(name=name)
        if function is None:
            err("VALUE", f"Unknown token '{name}'")
        else:
            return eval_function(name=function.name, params=function.params)

def get_function(name: str) -> metamodel["Function"] | None:
    for key, value in environment.items():
        if key == name and isinstance(value, metamodel["Function"]):
            return value
    return None

# Evaluate the parsed model
eval_model(model)
