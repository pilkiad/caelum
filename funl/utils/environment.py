# TODO - add module comment

from . import globalvars


def get_function_from_name(name: str) -> FunctionDefinition | None:
    for environment_function in globalvars.environment:
        if environment_function.name == name:
            return environment_function
    return None


def get_function_index_from_name(name: str) -> int | None:
    for i in range(0, len(globalvars.environment)):
        if globalvars.environment[i].name == name:
            return i
    return None


def append_or_update(function_definition: FunctionDefinition) -> None:
    result = get_function_index_from_name(function_definition.name)

    if result is not None:
        globalvars.environment[result] = function_definition
    else:
        globalvars.environment.append(function_definition)
