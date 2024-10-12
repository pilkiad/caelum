def handle(params: list[str]) -> str | None:
    """
    Funl function to evaluate statement and call a function if true.

    Example:
    eval(10, '<', 15, test)
    {params[0]} {params[1]} {params[2]} -> 10 < 15 -> True -> Return: test

    params: list[str]   param[0-2] will be used as a statement,
                        param[3] will be returned if the statement is True

    str | None          Name of the function to be called if
                        "{params[0]} {params[1]} {params[2]}" is True,
                        None otherwise
    """

    if eval(f"{params[0]} {params[1]} {params[2]}"):
        return params[3]

    return None
