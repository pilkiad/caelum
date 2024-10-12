def handle(params: list[str]) -> None:
    """
    Funl function to print given parameters to console.

    params: list[str]   List of strings that get printed
    """

    result = ""

    for param in params:
        print(str(param), end="")
        result += str(param)

    return result
