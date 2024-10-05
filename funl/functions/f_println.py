def handle(params: list[str]) -> None:
    """
    Funl function to print given parameters to console.
    After each paramter there will be a newline.

    params: list[str]   List of strings that get printed
    """
    
    result = ""

    for param in params:
        print(str(param))
        result += str(param)
    
    return result