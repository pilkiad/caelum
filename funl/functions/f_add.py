from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to add multiple integers.

    params: list[int]   The value of the integer, has to be a list since textx
                        parses all parameters as arrays
                        (even if there is only one)
    """

    if len(params) <= 1:
        logger.log_error("add", f"Invalid params: {params}")

    result = 0

    for param in params:
        try:
            value = int(param)
        except:
            logger.log_error("add", f"Invalid param: {param}")

        result += param

    return result
