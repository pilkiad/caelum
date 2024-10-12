from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to declare an integer by return the only given parameter as
    int.

    params: list[int]   The value of the integer, has to be a list since textx
                        parses all parameters as arrays
                        (even if there is only one)
    """

    if len(params) != 1:
        logger.log_error("int", f"Invalid params: {params}")

    try:
        value = int(params[0])
    except:
        logger.log_error("int", f"Invalid param: {params[0]}")

    return value
