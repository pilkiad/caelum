def handle(params: list[str]) -> str | None:
    """
    Funl function to evaluate statement and execute code block on True

    Example:
    eval(10, '<', 15, 'some code')
    {params[0]} {params[1]} {params[2]} -> 10 < 15 -> True -> Executes 'some code'

    NOTE - The code execution happens in the same environment as the parent function

    params: list[str]   param[0-2] will be used as a statement,
                        param[3] will be executed if the statement is True

    str | None          Name of the function to be called if
                        "{params[0]} {params[1]} {params[2]}" is True,
                        None otherwise
    """

    if params[0]:
        return params[1]

    return None
